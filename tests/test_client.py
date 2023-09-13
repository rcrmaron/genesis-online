import pytest
from .conftest import api_vcr, cassette_dir, delete_dir, TEST_DIR
from genesisonline import GenesisOnline
from genesisonline.constants import JsonKeys
from genesisonline.services import (
    TestService,
    FindService,
    CatalogueService,
    DataService,
    MetadataService,
)

cassette_subdir = str(cassette_dir / __name__.split(".")[-1])


@pytest.fixture
def api_client(credentials):
    username, password = credentials
    return GenesisOnline(username, password, language="en")


def test_service_count(api_client):
    assert len(api_client.services) == 5


def test_test_service_initialization(api_client):
    assert isinstance(api_client.test, TestService)


def test_find_service_initialization(api_client):
    assert isinstance(api_client.find, FindService)


def test_catalogue_service_initialization(api_client):
    assert isinstance(api_client.catalogue, CatalogueService)


def test_data_service_initialization(api_client):
    assert isinstance(api_client.data, DataService)


def test_metadata_service_initialization(api_client):
    assert isinstance(api_client.metadata, MetadataService)


def test_param_changing_consistent(api_client):
    api_client.username = "new_user"
    api_client.password = "new_password"
    api_client.language = "de"

    assert api_client.test._session.params["username"] == "new_user"
    assert api_client.find._session.params["password"] == "new_password"
    assert api_client.data._session.params["language"] == "de"


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_check_login_invalid_credentials(api_client):
    api_client.username = "invalid_user"
    api_client.password = "invalid_password"
    response = api_client.check_login()

    assert isinstance(response, dict)
    assert (
        response[JsonKeys.STATUS]
        == "An error has occured. (Your username or password is wrong.)"
    )
    assert response["Username"] == api_client.username


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_check_login(api_client):
    response = api_client.check_login()

    assert isinstance(response, dict)
    assert response[JsonKeys.STATUS] == "You have been logged in and out successfully!"
    assert response["Username"] == api_client.username


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_language_change(api_client):
    api_client.language = "de"
    response = api_client.check_login()

    assert isinstance(response, dict)
    assert response[JsonKeys.STATUS] == "Sie wurden erfolgreich an- und abgemeldet!"
    assert response["Username"] == api_client.username


@pytest.fixture(scope="module", autouse=True)
def cleanup_after_tests():
    yield
    delete_dir(TEST_DIR)
