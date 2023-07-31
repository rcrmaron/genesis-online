from typing import TYPE_CHECKING, Literal
import requests
from ..constants import BASE_URL
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
        url = self.BASE_URL + endpoint
        params = self._session.params | kwargs

        try:
            response = self._session.get(url, params=params)
            response.raise_for_status()  # Raise an exception for non-2xx status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            # Handle network-related errors
            print(f"Network error: {e}")
        except ValueError as e:
            # Handle JSON parsing errors
            print(f"JSON parsing error: {e}")
        except Exception as e:
            # Handle other unexpected errors
            print(f"Unexpected error: {e}")

        return None

    @abstractmethod
    def endpoints(self) -> list:
        """Return a list of all available endpoints for the service."""
        pass
