import requests
from typing import Any
from .constants import API_VERSION, JsonKeys
from .services import (
    TestService,
    FindService,
    CatalogueService,
    DataService,
    MetadataService,
)

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class GenesisOnline:
    """Object which represents the Genesis Online API.

    The RESTful web service is a collection of over 40 methods, which are
    structured in the following services:

    Attributes
    ----------
    test : TestService
        Service containing methods for testing the API.

    find : FindService
        Service containing methods for finding information.

    catalogue : CatalogueService
        Service containing methods for listing objects.

    data : DataService
        Service containing methods for retrieving data.

    metadata : MetadataService
        Service containing methods for retrieving metadata.

    services : list
        Overview of all registered services
    """

    version = API_VERSION

    def __init__(
        self, username: str, password: str, language: Literal["de", "en"] = "en"
    ) -> None:
        """Constructor for the GenesisOnline class.

        Parameters
        ----------
        username : str
            Name of the user according to the GENESIS account.

        password : str
            Password according to the GENESIS account.

        language : Literal['de', 'en'], default "en"
            Language the user wants the response to be in.
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
        self.data = DataService(self.session)
        self.metadata = MetadataService(self.session)
        self.services = [
            self.test._service,
            self.find._service,
            self.catalogue._service,
            self.data._service,
            self.metadata._service,
        ]

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

    def check_api(self) -> dict:
        """Check if API is online."""
        return self.test.whoami().get(JsonKeys.CONTENT)

    def check_login(self) -> dict:
        """Check if API login is valid."""
        return self.test.logincheck().get(JsonKeys.CONTENT)

    def request(self, endpoint: str, **kwargs) -> Any:
        """Returns unformatted response from specified API `endpoint`"""
        return self.test.request(endpoint, **kwargs)
