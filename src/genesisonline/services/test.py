"""Functionality for interacting with the GENESIS-Online HelloWorld service.
"""
import requests
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, JsonKeys, JsonStrings, ResponseStatus
from genesisonline.exceptions import StandardizationError


class TestService(BaseService):
    """Service containing methods for testing the API.

    This service is euqivalent to the 'HelloWorld' service from the GO-API.
    """

    __test__ = False  # mark for pytest (not a test class)

    _service = "helloworld"
    endpoints = ["whoami", "logincheck"]

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def __str__(self) -> str:
        return "Service containing methods for testing the API."

    def whoami(self, **api_params) -> dict:
        """Returns the IP address and the user agent of the caller.

        This allows to perform first tests of using the interface, without
        having to specify any parameters.
        """
        return self._request(Endpoints.TEST_WHOAMI, "whoami", **api_params)

    def logincheck(self, **api_params) -> dict:
        """Returns whether or not login using the account data was successful.

        This allows to perform first tests of using the interface, without
        having to look deeper into the specification
        """
        return self._request(Endpoints.TEST_LOGINCHECK, "logincheck", **api_params)

    def _request(self, endpoint: str, calling_method: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)
        try:
            return self._standardize_response(response, calling_method)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict, calling_method: str) -> dict:
        """Standaridze response according to wrapper guidelines."""
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
