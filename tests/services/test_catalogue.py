import pytest
import warnings
from genesisonline.services import CatalogueService
from genesisonline.exceptions import UnexpectedParameterWarning
from ..conftest import (
    api_vcr,
    cassette_dir,
    assert_match_found,
    assert_valid_json_structure,
    assert_background_task_found,
)

cassette_subdir = str(cassette_dir / __name__.split(".")[-1])


@pytest.fixture
def service(session):
    return CatalogueService(session)


def test_endpoints(service):
    assert len(service.endpoints) == 20


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cubes(service):
    api_params = {"selection": "124*", "area": "all", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.cubes(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cubes2statistic(service):
    api_params = {"name": "12411", "selection": "12411B*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.cubes2statistic(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cubes2variable(service):
    api_params = {"name": "KREISE", "selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.cubes2variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_jobs(service):
    api_params = {"selection": "", "pagelength": "20"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.jobs(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_modifieddata(service):
    api_params = {"selection": "", "type": "all", "date": "20.02.2020"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.modifieddata(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_qualitysigns(service):
    api_params = {}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.qualitysigns(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_results(service):
    api_params = {"selection": "", "area": "all", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.results(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_statistics(service):
    api_params = {"selection": "124*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.statistics(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_statistics2variable(service):
    api_params = {"name": "KREISE", "selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.statistics2variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_tables(service):
    api_params = {"selection": "124*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.tables(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_tables2statistics(service):
    api_params = {"name": "12411", "selection": "12411*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.tables2statistics(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_tables2variable(service):
    api_params = {"name": "KREISE", "selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.tables2variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_terms(service):
    api_params = {"selection": "Schu*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.terms(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_timeseries(service):
    api_params = {"selection": "124*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.timeseries(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_timeseries2statistic(service):
    api_params = {"name": "12411", "selection": "12411B*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.timeseries2statistic(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_timeseries2variable(service):
    api_params = {"name": "KREISE", "selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.timeseries2variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_values(service):
    api_params = {"selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.values(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_values2variable(service):
    api_params = {"name": "KREISE", "selection": "12*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.values2variable(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_variables(service):
    api_params = {"selection": "FA*", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.variables(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_variables2statistic(service):
    api_params = {"name": "12411", "pagelength": "1"}
    with warnings.catch_warnings(record=True) as warning_list:
        response = service.variables2statistic(**api_params)

    assert len(warning_list) == 0, f"Unexpected warning raised."
    assert_valid_json_structure(response)
    assert_match_found(response)


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_cubes_params_misspelled(service):
    api_params = {
        "selectionXYZ": "124*",
        "areaXYZ": "all",
        "pagelengthXYZ": "20",
    }
    with pytest.warns(UnexpectedParameterWarning):
        response = service.cubes(**api_params)
