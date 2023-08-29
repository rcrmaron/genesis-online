import pytest
from genesisonline.services import MetadataService
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
    return MetadataService(session)


def test_endpoints(service):
    assert len(service.endpoints) == 6


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cube(service):
    api_params = {"name": "12411BJ001", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.cube(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_statistic(service):
    api_params = {"name": "12411", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.statistic(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table(service):
    api_params = {"name": "12411-0001", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.table(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_timeseries(service):
    api_params = {"name": "12411BJ001", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.timeseries(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_value(service):
    api_params = {"name": "LEDIG", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.value(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_variable(service):
    api_params = {"name": "FAMSTD", "area": "all"}
    with pytest.warns(None) as warning_list:
        response = service.variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cube_params_misspelled(service):
    api_params = {"name": "12411BJ001", "areaXYZ": "all"}
    with pytest.warns(UnexpectedParameterWarning):
        response = service.cube(**api_params)
