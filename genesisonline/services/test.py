from typing import Literal
import requests
from .base import BaseService


class TestService(BaseService):
    def __init__(
        self,
        session: requests.Session,
        username: str,
        password: str,
        language: Literal["de", "en"] = "en",
    ) -> None:
        super().__init__(session, username, password, language)

    def endpoints(self) -> list:
        return ["whoami", "logincheck"]

    def whoami(self, **kwargs) -> dict:
        """Check if API is online."""
        return super()._request("test_whoami", **kwargs)

    def logincheck(self, **kwargs) -> dict:
        """Check if login is valid."""
        return super()._request("test_logincheck", **kwargs)
