"""
This module provides a base service as parent to all other services.

Classes:
    BaseService
"""

import requests
import warnings
from abc import ABC, abstractmethod
from typing import Any
from urllib.parse import urljoin
from genesisonline.constants import BASE_URL, JsonKeys
from genesisonline.exceptions import *


class BaseService(ABC):
    """Parent class for all services."""

    _BASE_URL = BASE_URL

    @property
    @abstractmethod
    def _service(self) -> str:
        """Name of service"""
        pass

    @property
    @abstractmethod
    def endpoints(self) -> list:
        """List of implemented endpoints for the service."""
        pass

    def __init__(self, session: requests.Session) -> None:
        """Initialize the service with a session.

        Parameters
        ----------
        session : requests.Session
            The session.params dictionary should contain:
            - "username" (str): The username for authentication.
            - "password" (str): The password for authentication.
        """
        self._session = session

    def _check_param_names(self, expected_params: list, received_params: list) -> None:
        """Check if API parameter names are as expected by the API.

        The GO-API response always includes a `Parameter` section where the
        expected parameters for an endpoint are listed. This is used here to
        verify the input parameters.

        Parameters
        ----------
        expected_params : list
            Parameter names as expected by the GO-API.
        received_params : list
            Parameter names as provided by the user during a call.

        Raises
        ------
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
        """Send a request to the specified Genesis-Online endpoint.

        Parameters
        ----------
        endpoint : str
            The endpoint URL segment to which the request will be sent.
        **api_params : dict
            Additional keyword arguments to be sent as query parameters in the request.

        Returns
        -------
        Any
            Depending on the content type, the returned content may be a JSON object,
            binary data, or text.

        Raises
        ------
        HTTPError
            This is raised when the HTTP request returned an unsuccessful status code.
        ConnectionError
            This is raised when the client is unable to connect to the server.
        TimeoutError
            This is raised when the request times out.
        RequestError
            This is raised for any other type of request exception.
        UnexpectedContentError
            If the content type of the response is not one of the expected content types.
            Expected types are application/json, image/png and text/csv.
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
        """For making requests, to be implemented by child classes.

        This method is meant to be overridden by child classes to handle their
        specific request needs.

        Returns
        -------
        dict
            A JSON dictionary containing the response data with the following
            key-value pairs:
            - "Ident": dict,
            - "Status": dict,
            - "Parameter": dict,
            - "Content": any,
            - "Copyright": str,

        Raises
        ------
        StandardizationError
            If the response data cannot be converted into the specified format.
        """
        pass
