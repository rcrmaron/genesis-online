"""
This module provides a service for testing the API.

It contains methods for checking the API's availability and verifying login credentials.

Classes:
    TestService
"""
import requests
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, JsonKeys, JsonStrings, ResponseStatus
from genesisonline.exceptions import StandardizationError


class TestService(BaseService):
    """Service containing methods for testing the API."""

    _service = "helloworld"
    endpoints = ["whoami", "logincheck"]

    def __init__(self, session: requests.Session) -> None:
        """Initialize the service with a session.

        Parameters
        ----------
        session : requests.Session
            The session.params dictionary should contain:
            - "username" (str): The username for authentication.
            - "password" (str): The password for authentication.
        """
        super().__init__(session)

    def __str__(self) -> str:
        return "Service containing methods for testing the API."

    def whoami(self, **api_params) -> dict:
        """Check if API is online.

        Parameters
        ----------
        **api_params
            Additional parameters for the API request.

        Returns
        -------
        A JSON dict standardized according to wrapper guidelines.
        """
        return self._request(Endpoints.TEST_WHOAMI, "whoami", **api_params)

    def logincheck(self, **api_params) -> dict:
        """Check if login is valid.

        Parameters
        ----------
        **api_params
            Additional parameters for the API request.

        Returns
        -------
        A JSON dict standardized according to wrapper guidelines.
        """
        return self._request(Endpoints.TEST_LOGINCHECK, "logincheck", **api_params)

    def _request(self, endpoint: str, calling_method: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)
        try:
            return self._standardize_response(response, calling_method)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict, calling_method: str) -> dict:
        """Standaridze response according to wrapper guidelines

        Parameters
        ----------
        response : dict
            JSON dict as returned from the GO-API.

        calling_method : str
            Name of the method invoking this function.

        Returns
        -------
        Contents of the original dict standardized according to wrapper guidelines.
        """
        standardized_response = {
            JsonKeys.IDENT: {
                JsonKeys.SERVICE: self._service,
                JsonKeys.METHOD: calling_method,
            },
            JsonKeys.STATUS: {
                JsonKeys.CODE: ResponseStatus.MATCH,
                JsonKeys.CONTENT: JsonStrings.NA,
                JsonKeys.TYPE: JsonStrings.NA,
            },
            JsonKeys.PARAMETER: {},
            JsonKeys.CONTENT: response,
            JsonKeys.COPYRIGHT: JsonStrings.NA,
        }
        return standardized_response
