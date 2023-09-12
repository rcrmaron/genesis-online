"""Functionality for interacting with the GENESIS-Online Catalogue service.
"""
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

    def cubes(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of cubes from `area` according to the `selection`."""
        return self._request(
            Endpoints.CATALOGUE_CUBES, selection=selection, area=area, **api_params
        )

    def cubes2statistic(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of cubes related to statistics `name` from `area` according to the `selection`."""
        return self._request(
            Endpoints.CATALOGUE_CUBES2STATISTIC,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def cubes2variable(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of cubes related to variable `name` from `area` according to the `selection`."""
        return self._request(
            Endpoints.CATALOGUE_CUBES2VARIABLE,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def jobs(self, selection: str = None, **api_params) -> dict:
        """Returns a list of batch jobs (i.e. very large tables) according to the parameters set."""
        return self._request(
            Endpoints.CATALOGUE_JOBS, selection=selection, **api_params
        )

    def modifieddata(self, selection: str = None, **api_params) -> dict:
        """Returns a list of objects, recently updated according to the parameters set."""
        return self._request(
            Endpoints.CATALOGUE_MODIFIEDDATA, selection=selection, **api_params
        )

    def qualitysigns(self, **api_params) -> dict:
        """Returns the list of quality characters from `area`"""  # TODO area is not documented in user documentation
        return self._request(Endpoints.CATALOGUE_QUALITYSIGNS, **api_params)

    def results(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of results tables from `area` according to the `selection`."""
        return self._request(
            Endpoints.CATALOGUE_RESULTS, selection=selection, area=area, **api_params
        )

    def statistics(self, selection: str = None, **api_params) -> dict:
        """Returns a list of statistics according to the parameters set."""
        return self._request(
            Endpoints.CATALOGUE_STATISTICS, selection=selection, **api_params
        )

    def statistics2variable(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of statistics related to variable `name` from `area`."""
        return self._request(
            Endpoints.CATALOGUE_STATISTICS2VARIABLE,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def tables(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of tables from `area` according to the parameters set"""
        return self._request(
            Endpoints.CATALOGUE_TABLES, selection=selection, area=area, **api_params
        )

    def tables2statistics(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of tables related to statistics `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TABLES2STATISTIC,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def tables2variable(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of tables related to variable `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TABLES2VARIABLE,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def terms(self, selection: str = None, **api_params) -> dict:
        """Returns a list of terms according to the `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TERMS, selection=selection, **api_params
        )

    def timeseries(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of timeseries from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TIMESERIES, selection=selection, area=area, **api_params
        )

    def timeseries2statistic(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of timeseries related to statistic `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TIMESERIES2STATISTIC,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def timeseries2variable(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of timeseries related to variable `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_TIMESERIES2VARIABLE,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def values(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of values from `area` according to the parameter set."""
        return self._request(
            Endpoints.CATALOGUE_VALUES, selection=selection, area=area, **api_params
        )

    def values2variable(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of values related to variable `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_VALUES2VARIABLE,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def variables(self, selection: str = None, area: str = None, **api_params) -> dict:
        """Returns a list of variables from `area` according to the parameter set."""
        return self._request(
            Endpoints.CATALOGUE_VARIABLES, selection=selection, area=area, **api_params
        )

    def variables2statistic(
        self, name: str = None, selection: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a list of variables related to statistic `name` from `area` according to `selection`."""
        return self._request(
            Endpoints.CATALOGUE_VARIABLES2STATISTIC,
            name=name,
            selection=selection,
            area=area,
            **api_params,
        )

    def _request(self, endpoint: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)

        try:
            return self._standardize_response(response)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict) -> dict:
        """Standaridze response according to wrapper guidelines."""
        copyright = response.pop(JsonKeys.COPYRIGHT)

        response[JsonKeys.CONTENT] = response.pop(JsonKeys.LIST)
        response[JsonKeys.COPYRIGHT] = copyright
        return response
