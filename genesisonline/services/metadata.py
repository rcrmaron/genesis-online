"""
This module provides a service for downloading metadata.

Classes:
    MetadataService
"""
import requests
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, JsonKeys
from genesisonline.exceptions import StandardizationError


class MetadataService(BaseService):
    """Service containing methods for downloading metadata."""

    _service = "metadata"
    endpoints = ["cube", "statistic", "table", "timeseries", "value", "variable"]

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def __str__(self) -> str:
        return "Service containing methods for downloading metadata."

    def cube(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the cube `name` from `area`."""
        return self._request(
            Endpoints.METADATA_CUBE, name=name, area=area, **api_params
        )

    def statistic(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the statistic `name` from `area`."""
        return self._request(
            Endpoints.METADATA_STATISTIC, name=name, area=area, **api_params
        )

    def table(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the table `name` from `area`."""
        return self._request(
            Endpoints.METADATA_TABLE, name=name, area=area, **api_params
        )

    def timeseries(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the timeseries `name` from `area`."""
        return self._request(
            Endpoints.METADATA_TIMESERIES, name=name, area=area, **api_params
        )

    def value(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the value `name` from `area`."""
        return self._request(
            Endpoints.METADATA_VALUE, name=name, area=area, **api_params
        )

    def variable(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns the metadata of the variable `name` from `area`."""
        return self._request(
            Endpoints.METADATA_VARIABLE, name=name, area=area, **api_params
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
        response[JsonKeys.CONTENT] = response.pop(JsonKeys.OBJECT)
        response[JsonKeys.COPYRIGHT] = copyright
        return response
