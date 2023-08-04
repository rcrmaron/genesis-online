import requests
from .base import BaseService
from ..constants import Endpoints
from ..utils import get_api_params


class CatalogueService(BaseService):
    """Service containing methods for listing objects"""

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
        """Returns a list of cubes from `area` according to the parameters set.

        Parameters
        ----------
        selection : str
            Filters the cubes whose code matches `selection`.
            Between 1-10 characters, supports "*"-notation.

        area : str
            Domain where the object is stored.

        pagelength : str
            Maximum number of items that will be returned. Can be between 1-2500.
            defaults to 100 if `pagelength` is None.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_CUBES, **api_params)

    def cubes2statistic(
        self,
        name: str = None,
        selection: str = None,
        area: str = None,
        pagelength: str = None,
        **kwargs
    ) -> dict:
        """Returns a list of cubes related to the statistics `name` from `area`
        according to the parameters set.

        Parameters
        ----------
        name : str
            Name of the statistics. Between 1-6 characters.

        selection : str
            Filters the cubes whose code matches `selection`.
            Between 1-10 characters, supports "*"-notation.

        area : str
            Domain where the object is stored.

        pagelength : str
            Maximum number of items that will be returned. Can be between 1-2500.
            defaults to 100 if `pagelength` is None.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_CUBES2STATISTIC, **api_params)

    def cubes2variable(
        self,
        name: str = None,
        selection: str = None,
        area: str = None,
        pagelength: str = None,
        **kwargs
    ) -> dict:
        """Returns a list of cubes related to variable `name` from `area`
        according to the parameters set.

        Parameters
        ----------
        name : str
            Name of the statistics. Between 1-6 characters.

        selection : str
            Filters the cubes whose code matches `selection`.
            Between 1-10 characters, supports "*"-notation.

        area : str
            Domain where the object is stored.

        pagelength : str
            Maximum number of items that will be returned. Can be between 1-2500.
            defaults to 100 if `pagelength` is None.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_CUBES2VARIABLE, **api_params)

    def jobs(self, selection, **kwargs) -> dict:
        """Delivers a list of jobs."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_JOBS, **api_params)

    def modifieddata(self, **kwargs) -> dict:
        """Delivers a list of modified objects."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_MODIFIEDDATA, **api_params)

    def qualitysigns(self, **kwargs) -> dict:
        """Delivers a list of quality signs."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_QUALITYSIGNS, **api_params)

    def results(self, **kwargs) -> dict:
        """Delivers a list of results."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_RESULTS, **api_params)

    def statistics(self, **kwargs) -> dict:
        """Delivers a list of statistics."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_STATISTICS, **api_params)

    def statistics2variable(self, **kwargs) -> dict:
        """Delivers a list of statistics for a variable."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_STATISTICS2VARIABLE, **api_params)

    def tables(self, **kwargs) -> dict:
        """Delivers a list of tables."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TABLES, **api_params)

    def tables2statistics(self, **kwargs) -> dict:
        """Delivers a list of tables for a statistic."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TABLES2STATISTICS, **api_params)

    def tables2variables(self, **kwargs) -> dict:
        """Delivers a list of tables for a variable."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TERMS, **api_params)

    def terms(self, **kwargs) -> dict:
        """Delivers a list of terms."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TERMS, **api_params)

    def timeseries(self, **kwargs) -> dict:
        """Delivers a list of time series."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TIMESERIES, **api_params)

    def timeseries2statistic(self, **kwargs) -> dict:
        """Delivers a list of time series for a statistic."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TIMESERIES2STATISTICS, **api_params)

    def timeseries2variable(self, **kwargs) -> dict:
        """Delivers a list of time series for a variable."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_TIMESERIES2VARIABLES, **api_params)

    def values(self, **kwargs) -> dict:
        """Delivers a list of values."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_VALUES, **api_params)

    def values2variable(self, **kwargs) -> dict:
        """Delivers a list of values for a variable."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_VALUES2VARIABLE, **api_params)

    def variables(self, **kwargs) -> dict:
        """Delivers a list of variables."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_VARIABLES, **api_params)

    def variables2statistic(self, **kwargs) -> dict:
        """Delivers a list of variables for a statistic."""
        api_params = get_api_params(locals())
        return super()._request(Endpoints.CATALOGUE_VARIABLES2STATISTIC, **api_params)
