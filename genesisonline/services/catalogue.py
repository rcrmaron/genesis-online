import requests
from .base import BaseService
from ..constants import Endpoints


class CatalogueService(BaseService):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return [
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

    def cubes(
        self, selection: str = None, area: str = None, pagelength: str = None, **kwargs
    ) -> dict:
        """Delivers a list of data cubes."""
        return super()._request(Endpoints.CATALOGUE_CUBES, **kwargs)

    def cubes2statistic(
        self,
        name: str = None,
        selection: str = None,
        area: str = None,
        pagelength: str = None,
        **kwargs
    ) -> dict:
        """Delivers a list of data cubes for a statistic."""
        return super()._request(Endpoints.CATALOGUE_CUBES2STATISTIC, **kwargs)

    def cubes2variable(
        self,
        name: str = None,
        selection: str = None,
        area: str = None,
        pagelength: str = None,
        **kwargs
    ) -> dict:
        """Delivers a list of data cubes for a variable."""
        return super()._request(Endpoints.CATALOGUE_CUBES2VARIABLE, **kwargs)

    def jobs(self, selection, **kwargs) -> dict:
        """Delivers a list of jobs."""
        return super()._request(Endpoints.CATALOGUE_JOBS, **kwargs)

    def modifieddata(self, **kwargs) -> dict:
        """Delivers a list of modified objects."""
        return super()._request(Endpoints.CATALOGUE_MODIFIEDDATA, **kwargs)

    def qualitysigns(self, **kwargs) -> dict:
        """Delivers a list of quality signs."""
        return super()._request(Endpoints.CATALOGUE_QUALITYSIGNS, **kwargs)

    def results(self, **kwargs) -> dict:
        """Delivers a list of results."""
        return super()._request(Endpoints.CATALOGUE_RESULTS, **kwargs)

    def statistics(self, **kwargs) -> dict:
        """Delivers a list of statistics."""
        return super()._request(Endpoints.CATALOGUE_STATISTICS, **kwargs)

    def statistics2variable(self, **kwargs) -> dict:
        """Delivers a list of statistics for a variable."""
        return super()._request(Endpoints.CATALOGUE_STATISTICS2VARIABLE, **kwargs)

    def tables(self, **kwargs) -> dict:
        """Delivers a list of tables."""
        return super()._request(Endpoints.CATALOGUE_TABLES, **kwargs)

    def tables2statistics(self, **kwargs) -> dict:
        """Delivers a list of tables for a statistic."""
        return super()._request(Endpoints.CATALOGUE_TABLES2STATISTICS, **kwargs)

    def tables2variables(self, **kwargs) -> dict:
        """Delivers a list of tables for a variable."""
        return super()._request(Endpoints.CATALOGUE_TERMS, **kwargs)

    def terms(self, **kwargs) -> dict:
        """Delivers a list of terms."""
        return super()._request(Endpoints.CATALOGUE_TERMS, **kwargs)

    def timeseries(self, **kwargs) -> dict:
        """Delivers a list of time series."""
        return super()._request(Endpoints.CATALOGUE_TIMESERIES, **kwargs)

    def timeseries2statistic(self, **kwargs) -> dict:
        """Delivers a list of time series for a statistic."""
        return super()._request(Endpoints.CATALOGUE_TIMESERIES2STATISTICS, **kwargs)

    def timeseries2variable(self, **kwargs) -> dict:
        """Delivers a list of time series for a variable."""
        return super()._request(Endpoints.CATALOGUE_TIMESERIES2VARIABLES, **kwargs)

    def values(self, **kwargs) -> dict:
        """Delivers a list of values."""
        return super()._request(Endpoints.CATALOGUE_VALUES, **kwargs)

    def values2variable(self, **kwargs) -> dict:
        """Delivers a list of values for a variable."""
        return super()._request(Endpoints.CATALOGUE_VALUES2VARIABLE, **kwargs)

    def variables(self, **kwargs) -> dict:
        """Delivers a list of variables."""
        return super()._request(Endpoints.CATALOGUE_VARIABLES, **kwargs)

    def variables2statistic(self, **kwargs) -> dict:
        """Delivers a list of variables for a statistic."""
        return super()._request(Endpoints.CATALOGUE_VARIABLES2STATISTIC, **kwargs)
