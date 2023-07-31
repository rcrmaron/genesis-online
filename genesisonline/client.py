import requests
from typing import Literal
from .constants import API_VERSION
from .services import TestService, FindService, CatalogueService


class GenesisOnline:
    """Object which represents the Genesis Online API."""

    VERSION = API_VERSION

    def __init__(
        self, username: str, password: str, language: Literal["de", "en"] = "en"
    ) -> None:
        """Constructor for the GenesisOnline class.

        Parameters
        ----------
        username : str
            Username for login

        password : str
            Password for login

        language : Literal['de', 'en'], default "en"
            Language for the API results
        """
        self.session = requests.Session()
        self.session.params = {
            "username": username,
            "password": password,
            "language": language,
        }
        self.username = username
        self.password = password
        self.language = language
        self.test = TestService(self.session)
        self.find = FindService(self.session)
        self.catalogue = CatalogueService(self.session)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value
        self.session.params["username"] = value

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value
        self.session.params["password"] = value

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value: Literal["de", "en"]):
        self._language = value
        self.session.params["language"] = value

    def services(self) -> list:
        """Return a list of all available services."""
        return ["test", "find", "catalogue"]

    def check_api(self) -> dict:
        """Check if API is online."""
        return self.test.whoami()

    def check_login(self) -> dict:
        """Check if login is valid."""
        return self.test.logincheck()

    def manual_request(self, url: str) -> dict:
        """Manually request an API endpoint by providing a preformatted URL.

        This method is mainly intendended for debugging/testing purposes.

        Parameters
        ----------
        url : str
            Preformatted URL to request (requires manual formatting of parameters)

        Returns
        -------
        dict : JSON response from the API
        """
        response = self.session.get(url)
        return response.json()
