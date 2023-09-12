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
    """Object which represents the GENESIS-Online API.

    The RESTful web service is a collection of over 40 methods, which are
    structured in the following attributes.

    Attributes:
        test (TestService): Service containing methods for testing the API.
        find (FindService): Service containing methods for finding information.
        catalogue (CatalogueService): Service containing methods for listing objects.
        data (DataService): Service containing methods for retrieving data.
        metadata (MetadataService): Service containing methods for retrieving metadata.
        services (list): Overview of all available services.
    """

    version = API_VERSION

    def __init__(
        self, username: str, password: str, language: Literal["de", "en"] = "en"
    ) -> None:
        """Constructor for the `GenesisOnline` class.

        Args:
            username: username of the user's GENESIS-Online account.
            password: password of the user's GENESIS-Online account.
            language: language the user wants the response to be in.
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
        """Username of the user's GENESIS-Online account."""
        return self._username

    @username.setter
    def username(self, value: str):
        self._username = value
        self.session.params["username"] = value

    @property
    def password(self):
        """Password of the user's GENESIS-Online account."""
        return self._password

    @password.setter
    def password(self, value: str):
        self._password = value
        self.session.params["password"] = value

    @property
    def language(self):
        """Language the user wants the response to be in."""
        return self._language

    @language.setter
    def language(self, value: Literal["de", "en"]):
        self._language = value
        self.session.params["language"] = value

    def check_api(self) -> dict:
        """Check if the GENESIS-Online API is online."""
        return self.test.whoami().get(JsonKeys.CONTENT)

    def check_login(self) -> dict:
        """Check if the GENESIS-Online API credentials are valid."""
        return self.test.logincheck().get(JsonKeys.CONTENT)

    def request(self, endpoint: str, **kwargs: str) -> Any:
        """Returns a raw response from the specified `endpoint`.

        This function can be used to retrieve a completely unformatted response
        from the GENESIS-Online API. This ensures that endpoints which are not
        yet implemented can be accessed.

        Args:
            endpoint: The endpoint URL segment to which the request will be sent.
            **kwargs: Additional keyword arguments to be sent as query parameters
                in the request.

        Returns:
            Any: The returned content may be a JSON, binary or text.

        Raises:
            HTTPError: When the HTTP request returns an unsuccessful status code.
            ConnectionError: When the client is unable to connect to the server.
            TimeoutError: When the request times out.
            RequestError: For any other type of request exception.
            UnexpectedContentError: If the content type of the response is not
                one of the expected content types. Expected types are
                'application/json', 'image/png' and 'text/csv'.

        Examples:
            >>> from genesisonline import GenesisOnline
            >>>
            >>> # request to get raw 'image/png' from the data service
            >>> go = GenesisOnline(username="your_username", password="your_password")
            >>> response = go.request(endpoint="data/chart2table", name="12411-0001")
            >>> print(response)
        """
        return self.test.request(endpoint, **kwargs)
