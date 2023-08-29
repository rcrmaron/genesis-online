import requests
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, JsonKeys
from genesisonline.exceptions import StandardizationError


class FindService(BaseService):
    """Service containing methods for finding information on objects.

    Objects can be cubes, statistics, tables, timeseries or variables.
    """

    _service = "find"
    endpoints = ["find"]

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def __str__(self) -> str:
        return "Service containing methods for finding information on objects."

    def find(self, term: str, **api_params) -> dict:
        return self._request(Endpoints.FIND_FIND, term=term, **api_params)

    def _request(self, endpoint: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)

        try:
            return self._standardize_response(response)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict) -> dict:
        copyright = response.pop(JsonKeys.COPYRIGHT)

        response[JsonKeys.CONTENT] = {
            JsonKeys.CUBES: response.pop(JsonKeys.CUBES),
            JsonKeys.STATISTICS: response.pop(JsonKeys.STATISTICS),
            JsonKeys.TABLES: response.pop(JsonKeys.TABLES),
            JsonKeys.TIMESERIES: response.pop(JsonKeys.TIMESERIES),
            JsonKeys.VARIABLES: response.pop(JsonKeys.VARIABLES),
        }
        response[JsonKeys.COPYRIGHT] = copyright
        return response
