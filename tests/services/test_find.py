import pytest
import warnings
from genesisonline.services import FindService
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
    return FindService(session)


def test_endpoints(service):
    assert len(service.endpoints) == 1


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_find(service):
    api_params = {"term": "waste", "category": "cubes", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.find(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


def test_find_params_misspelled(service):
    api_params = {"term": "waste", "categoryXYZ": "cubes", "pagelengthXYZ": "1"}
    with pytest.warns(UnexpectedParameterWarning):
        response = service.find(**api_params)

    assert_valid_json_structure(response)
    assert_match_found(response)
