import requests
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, JsonKeys
from genesisonline.exceptions import StandardizationError


class CatalogueService(BaseService):
    """Service containing methods for listing objects."""

    _service = "catalogue"
    endpoints = [
        "cubes",
        "cubes2statistic",
        "cubes2variable",
        "jobs",
        "modifieddata",
        "qualitysigns",
        "results",
        "statistics",
        "statistics2variable",
        "tables",
        "tables2statistics",
        "tables2variables",
        "terms",
        "timeseries",
        "timeseries2statistic",
        "timeseries2variable",
        "values",
        "values2variable",
        "variables",
        "variables2statistic",
    ]

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def __str__(self) -> str:
        return "Service containing methods for listing objects."

    def cubes(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_CUBES, **api_params)

    def cubes2statistic(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_CUBES2STATISTIC, **api_params)

    def cubes2variable(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_CUBES2VARIABLE, **api_params)

    def jobs(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_JOBS, **api_params)

    def modifieddata(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_MODIFIEDDATA, **api_params)

    def qualitysigns(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_QUALITYSIGNS, **api_params)

    def results(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_RESULTS, **api_params)

    def statistics(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_STATISTICS, **api_params)

    def statistics2variable(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_STATISTICS2VARIABLE, **api_params)

    def tables(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TABLES, **api_params)

    def tables2statistics(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TABLES2STATISTIC, **api_params)

    def tables2variable(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TABLES2VARIABLE, **api_params)

    def terms(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TERMS, **api_params)

    def timeseries(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TIMESERIES, **api_params)

    def timeseries2statistic(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TIMESERIES2STATISTIC, **api_params)

    def timeseries2variable(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_TIMESERIES2VARIABLE, **api_params)

    def values(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_VALUES, **api_params)

    def values2variable(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_VALUES2VARIABLE, **api_params)

    def variables(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_VARIABLES, **api_params)

    def variables2statistic(self, **api_params) -> dict:
        return self._request(Endpoints.CATALOGUE_VARIABLES2STATISTIC, **api_params)

    def _request(self, endpoint: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)

        try:
            return self._standardize_response(response)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict) -> dict:
        copyright = response.pop(JsonKeys.COPYRIGHT)

        response[JsonKeys.CONTENT] = response.pop(JsonKeys.LIST)
        response[JsonKeys.COPYRIGHT] = copyright
        return response
