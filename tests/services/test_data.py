import pytest
import warnings
from genesisonline.services import DataService
from genesisonline.services.base import UnexpectedParameterWarning
from ..conftest import (
    TEST_DIR,
    api_vcr,
    cassette_dir,
    assert_match_found,
    assert_valid_json_structure,
    assert_no_match_found,
    assert_background_task_found,
    delete_dir,
)

cassette_subdir = str(cassette_dir / __name__.split(".")[-1])


@pytest.fixture
def service(session):
    return DataService(session)


def test_endpoints(service):
    assert len(service.endpoints) == 10


# @api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
# def test_chart2result(service):
#     api_params = {"name": "12411-0001"}
#     with warnings.catch_warnings(record=True) as warning_list:
#         response = service.chart2result(**api_params)

#     assert len(warning_list) == 0, f"Unexpected warning raised."
#     assert_valid_json_structure(response)
#     assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_chart2table(service):
    api_params = {"name": "12411-0001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.chart2table(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_chart2timeseries(service):
    api_params = {"name": "11111LJ001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.chart2timeseries(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cube(service):
    api_params = {"name": "11111BJ001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.cube(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


# @api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
# def test_map2result(service):
#     api_params = {}
#     with warnings.catch_warnings(record=True) as warning_list:
#         response = service.map2result(**api_params)

#     assert len(warning_list) == 0, f"Unexpected warning raised."
#     assert_valid_json_structure(response)
#     assert_match_found(response)


def test_map2table(service):
    api_params = {"name": "11111-0001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.map2table(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_map2timeseries(service):
    api_params = {"name": "11111KJ001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.map2timeseries(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


# @api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
# def test_result(service):
#     api_params = {"name": "51000-0013"}
#     with warnings.catch_warnings(record=True) as warning_list:
#         response = service.table(wait_for_result=False, **api_params)
#         response = service.result(name=response["Content"]["ID"])

#     assert len(warning_list) == 0, f"Unexpected warning raised."
#     assert_valid_json_structure(response)
#     assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table_small(service):
    api_params = {"name": "51000-0012"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.table(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table_small_not_found(service):
    api_params = {"name": "51000-ABCD"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.table(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_no_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table_large_synchronous(service):
    # reduce timeout to avoid RemoteDisconnectd area during testing
    service._timeout = 10
    api_params = {"name": "51000-0013"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.table(wait_for_result=True, **api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)
    # assert not response["Content"].startswith("Result not yet available.")


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table_large_asynchronous(service):
    api_params = {"name": "51000-0013"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.table(wait_for_result=False, **api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    # assert_match_found(response)
    assert_background_task_found(response)
    # assert response["Content"].startswith("Result not yet available.")


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_timeseries(service):
    api_params = {"name": "11111KJ001"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.timeseries(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_table_params_misspelled(service):
    api_params = {"name": "12411-0001", "selectionXYZ": "all"}
    with pytest.warns(UnexpectedParameterWarning):
        response = service.table(**api_params)


@pytest.fixture(scope="session", autouse=True)
def cleanup_after_tests():
    yield
    delete_dir(TEST_DIR)
