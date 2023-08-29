import pytest
from genesisonline.services import TestService
from genesisonline.exceptions import UnexpectedParameterWarning
from ..conftest import (
    api_vcr,
    cassette_dir,
    assert_match_found,
    assert_valid_json_structure,
)

cassette_subdir = str(cassette_dir / __name__.split(".")[-1])


@pytest.fixture
def service(session):
    return TestService(session)


def test_endpoints(service):
    assert len(service.endpoints) == 2


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_whoami(service):
    with pytest.warns(None) as warning_list:
        response = service.whoami()

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_logincheck(service):
    with pytest.warns(None) as warning_list:
        response = service.logincheck()

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)
