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

    def cube(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_CUBE, name=name, **api_params)

    def statistic(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_STATISTIC, name=name, **api_params)

    def table(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_TABLE, name=name, **api_params)

    def timeseries(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_TIMESERIES, name=name, **api_params)

    def value(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_VALUE, name=name, **api_params)

    def variable(self, name: str, **api_params) -> dict:
        return self._request(Endpoints.METADATA_VARIABLE, name=name, **api_params)

    def _request(self, endpoint: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)

        try:
            return self._standardize_response(response)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict) -> dict:
        copyright = response.pop(JsonKeys.COPYRIGHT)
        response[JsonKeys.CONTENT] = response.pop(JsonKeys.OBJECT)
        response[JsonKeys.COPYRIGHT] = copyright
        return response
