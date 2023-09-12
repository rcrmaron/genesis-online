"""This module provides the foundational service class for the GENESIS-Online API wrapper.

The `BaseService` class serves as the parent class for all service classes that
interact with the GENESIS-Online API. It provides common methods for sending 
requests, handling responses, and validating parameters against the 
GENESIS-Online API's expectations.

An abstract base class that defines the core functionalities 
        for interacting with the GENESIS-Online API. All specific service
        classes should inherit from this base class and implement the required
        abstract methods.
"""

import requests
import warnings
from abc import ABC, abstractmethod
from typing import Any
from urllib.parse import urljoin
from genesisonline.constants import BASE_URL, JsonKeys
from genesisonline.exceptions import *


class BaseService(ABC):
    """Parent class for all GENESIS-Online service classes.

    An abstract base class that defines the core functionalities for interacting
    with the GENESIS-Online API. All specific service classes should inherit
    from this base class and implement the required abstract methods.
    """

    _BASE_URL = BASE_URL

    @property
    @abstractmethod
    def _service(self) -> str:
        """Name of GENESIS-Online service"""
        pass

    @property
    @abstractmethod
    def endpoints(self) -> list:
        """List of implemented endpoints for the GENESIS-Online service."""
        pass

    def __init__(self, session: requests.Session) -> None:
        """Initialize the service with a session.

        Args:
            session: session object with a 'params' dictionary attribute
                containing the keys:<br>
                - username (str): The username for authentication.<br>
                - password (str): The password for authentication.<br>
        """
        self._session = session

    def _check_param_names(self, expected_params: list, received_params: list) -> None:
        """Check if parameter names are as expected by the GENESIS-Online API.

        The GENESIS-Online API response always includes a `Parameter` section
        where the expected parameters for an endpoint are listed. This is used
        here to verify the input parameters.

        Args:
            expected_params: parameter names as expected by the GENESIS-Online API.
            received_params: parameter names as provided by the user.

        Raises:
            UnexpectedParameterWarning
        """
        mismatched_params = list()

        for param in received_params:
            if param not in expected_params:
                mismatched_params.append(param)

        if mismatched_params:
            warnings.warn(
                f"Received {mismatched_params}. Expected one of {expected_params}",
                UnexpectedParameterWarning,
            )

    def request(self, endpoint: str, **api_params) -> Any:
        """Send a request to the specified GENESIS-Online endpoint.

        Args:
            endpoint: the endpoint URL segment to which the request will be sent.
            **api_params: additional keyword arguments to be sent as query
                parameters in the request.

        Returns:
            Any: depending on the content type, the returned content may be a
                JSON object, binary data, or text.

        Raises:
            HTTPError: when the HTTP request returns an unsuccessful status code.
            ConnectionError: when the client is unable to connect to the server.
            TimeoutError: when the request times out.
            RequestError: for any other type of request exception.
            UnexpectedContentError: if the content type of the response is not
                one of the expected content types. Expected types are
                application/json, image/png and text/csv.
        """
        url = urljoin(self._BASE_URL, endpoint)
        try:
            response = self._session.get(url, params=api_params)
            response.raise_for_status()

            content_type = response.headers.get("content-type")
            if "application/json" in content_type:
                content = response.json()
                self._check_param_names(
                    expected_params=list(content.get(JsonKeys.PARAMETER, {}).keys()),
                    received_params=list(api_params.keys()),
                )
            elif "image/png" in content_type:
                content = response.content
            elif "text/csv" in content_type:
                content = response.text
            else:
                raise UnexpectedContentError(f"Unexpected content type: {content_type}")
            return content
        except requests.exceptions.HTTPError as e:
            raise HTTPError(f"HTTP error occurred: {e}") from e
        except requests.exceptions.ConnectionError as e:
            raise ConnectionError(f"Connection error occurred: {e}") from e
        except requests.exceptions.Timeout as e:
            raise TimeoutError(f"Timeout error occurred: {e}") from e
        except requests.exceptions.RequestException as e:
            raise RequestError(f"Request error occurred: {e}") from e

    @abstractmethod
    def _request(self) -> dict:
        """For making requests, to be implemented by all child classes.

        This method is meant to be overridden by child classes to handle their
        specific request needs.

        Returns:
            A JSON dictionary containing the response data with the following
            key-value pairs:
            - "Ident": dict,
            - "Status": dict,
            - "Parameter": dict,
            - "Content": any,
            - "Copyright": str,

        Raises:
            StandardizationError: if the response data cannot be converted into
                the specified format.
        """
        pass
