from typing import TYPE_CHECKING, Literal
import requests
from ..constants import ENDPOINT_PATHS, BASE_URL
from abc import ABC, abstractmethod


class BaseService(ABC):
    BASE_URL = BASE_URL

    def __init__(self, session: requests.Session) -> None:
        """Constructor for the GenesisOnlineBase class.

        Parameters
        ----------
        session : requests.Session
            Session for all requests
        """
        self._session = session

    def _request(self, endpoint: str, **kwargs) -> dict:
        url = self.BASE_URL + ENDPOINT_PATHS[endpoint]
        params = self._session.params | kwargs

        response = self._session.get(url, params=params)
        print(f"Requesting from {response.url}")
        return response.json()

    @abstractmethod
    def endpoints(self) -> list:
        """Return a list of all available endpoints for the service."""
        pass
