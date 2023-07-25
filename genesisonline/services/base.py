from typing import TYPE_CHECKING, Literal
import requests
from ..constants import ENDPOINT_PATHS, BASE_URL
from abc import ABC, abstractmethod


class BaseService(ABC):
    BASE_URL = BASE_URL

    def __init__(
        self,
        session: requests.Session,
        username: str,
        password: str,
        language: Literal["de", "en"] = "en",
    ) -> None:
        """Constructor for the GenesisOnlineBase class.

        Parameters
        ----------
        session : requests.Session
            Session for all requests

        username : str
            Username for login

        password : str
            Password for login

        language : Literal['de', 'en'], default "en"
            Language for the API
        """
        self._session = session
        self._username = username
        self._password = password
        self._language = language
        self.base_params = {
            "username": self._username,
            "password": self._password,
            "language": self._language,
        }

    def _request(self, endpoint: str, **kwargs) -> dict:
        url = self.BASE_URL + ENDPOINT_PATHS[endpoint]
        params = self.base_params | kwargs

        response = self._session.get(url, params=params)
        print(f"Requesting from {response.url}")
        return response.json()

    @abstractmethod
    def endpoints(self) -> list:
        """Return a list of all available endpoints for the service."""
        pass
