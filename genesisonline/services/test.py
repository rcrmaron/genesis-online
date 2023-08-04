import requests
from .base import BaseService
from ..constants import Endpoints
from ..utils import get_api_params


class TestService(BaseService):
    """Service containing methods for testing the API"""

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return ["whoami", "logincheck"]

    def whoami(self, **kwargs) -> dict:
        """Check if API is online.

        Returns
        -------
        The IP address and the user agent of the caller.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.TEST_WHOAMI, **api_params)

    def logincheck(self, **kwargs) -> dict:
        """Check if login is valid.

        Returns
        -------
        Whether or not login using the account data was successful.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.TEST_LOGINCHECK, **api_params)
