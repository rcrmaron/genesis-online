import os
import pytest
import configparser
import vcr
import requests
from pathlib import Path
from genesisonline.constants import JsonKeys, ResponseStatus, PACKAGE_NAME

TEST_DIR = Path(os.path.expanduser("~")) / PACKAGE_NAME


@pytest.fixture
def credentials():
    config_path = Path(__file__).parent.parent / "auth.ini"
    if not config_path.exists():
        raise FileNotFoundError(f"The config file '{config_path}' does not exist.")

    config = configparser.ConfigParser()
    config.read(config_path)
    username = config.get("Credentials", "username")
    password = config.get("Credentials", "password")

    return username, password


@pytest.fixture
def session(credentials):
    username, password = credentials
    session = requests.Session()
    session.params = {
        "username": username,
        "password": password,
        "language": "en",
    }

    return session


cassette_dir = Path(__file__).parent / "cassettes"
api_vcr = vcr.VCR(
    record_mode="once",  # NOTE change to 'all' when developing tests
    path_transformer=vcr.VCR.ensure_suffix(".yaml"),
    filter_query_parameters=["username", "password"],
)


def api_param_names_valid(params_in, params_out):
    """Verify if the provided function parameters are as expected by the API.

    When called by an endpoint, the Genesis Online API returns a response
    containing a dict of legal parameter names and values (i.e. `params_out`).
    This can be used as a template to check whether the supplied named parameters
    (i.e. `params_in`) exist and are correctly spelled.
    """
    for key in params_in.keys():
        if key not in params_out.keys():
            return False
    return True


def assert_valid_json_structure(response):
    assert isinstance(
        response, dict
    ), f"Expected type 'dict' but got type {type(response).__name__}"

    assert JsonKeys.IDENT in response
    assert JsonKeys.STATUS in response
    assert JsonKeys.PARAMETER in response
    assert JsonKeys.CONTENT in response
    assert JsonKeys.COPYRIGHT in response


def assert_match_found(response):
    status = response[JsonKeys.STATUS][JsonKeys.CODE]
    assert status == ResponseStatus.MATCH or status == ResponseStatus.PARTLY_MATCH
    assert response[JsonKeys.CONTENT] is not None


def assert_no_match_found(response):
    status = response[JsonKeys.STATUS][JsonKeys.CODE]
    assert status == ResponseStatus.NO_MATCH
    assert response[JsonKeys.CONTENT] is None


def assert_background_task_found(response):
    status = response[JsonKeys.STATUS][JsonKeys.CODE]
    assert status == ResponseStatus.BACKGROUND_RUN
    assert response[JsonKeys.CONTENT] is not None


def delete_dir(directory: Path) -> None:
    """Utility function for deleting a directory includign files"""
    for file in directory.iterdir():
        file.unlink()
    directory.rmdir()
