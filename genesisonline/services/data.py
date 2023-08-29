import requests
import time
import re
from threading import Thread
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, ResponseStatus, JsonKeys
from genesisonline.exceptions import StandardizationError

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal


class DataService(BaseService):
    """Service containing methods for downloading data."""

    _service = "data"
    endpoints = [
        "chart2result",
        "chart2table",
        "chart2timeseries",
        "cube",
        "map2result",
        "map2table",
        "map2timeseries",
        "result",
        "table",
        "timeseries",
    ]
    _cache = dict()

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)
        self._timeout = 30

    def __str__(self) -> str:
        return "Service containing methods for downloading data."

    def load(self, result_id):
        return self._cache.get(
            result_id, f"No entry for result '{result_id}'"
        )  # TODO save as file, custom error?

    def save(self, result_id, object):
        self._cache[result_id] = object

    def chart2result(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_CHART2RESULT, **api_params)

    def chart2table(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_CHART2TABLE, **api_params)

    def chart2timeseries(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_CHART2TIMESERIES, **api_params)

    def cube(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_CUBE, **api_params)

    def map2result(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_MAP2RESULT, **api_params)

    def map2table(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_MAP2TABLE, **api_params)

    def map2timeseries(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_MAP2TIMESERIES, **api_params)

    def result(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_RESULT, **api_params)

    def table(self, wait_for_result: bool = True, **api_params) -> dict:
        response = self._request(Endpoints.DATA_TABLE, job="true", **api_params)

        if response["Status"]["Code"] == ResponseStatus.BACKGROUND_RUN:
            return self._get_batch_job_result(response, wait_for_result)
        return response

    def timeseries(self, **api_params) -> dict:
        return self._request(Endpoints.DATA_TIMESERIES, **api_params)

    def _request(self, endpoint: str, **api_params) -> dict:
        response = super().request(endpoint, **api_params)

        # check if non-empty json object
        if isinstance(response, dict) and response[JsonKeys.OBJECT]:
            # get rid of nested structure (standardization)
            response[JsonKeys.OBJECT] = response[JsonKeys.OBJECT][JsonKeys.CONTENT]

        # check if non-json object i.e. image or text file
        if not isinstance(response, dict):
            content = response  # rename response to something more descriptive
            response = self._get_json_container(endpoint, api_params)
            response[JsonKeys.OBJECT] = content

        try:
            return self._standardize_response(response)
        except Exception as e:
            raise StandardizationError(f"Standardization error occured: {e}") from e

    def _standardize_response(self, response: dict) -> dict:
        copyright = response.pop(JsonKeys.COPYRIGHT)
        response[JsonKeys.CONTENT] = response.pop(JsonKeys.OBJECT)
        response[JsonKeys.COPYRIGHT] = copyright
        return response

    def _get_json_container(self, endpoint: str, api_params: dict) -> dict:
        """Get an empty GO json container"""

        # make API call with invalid parameters to get an empty "json containter"
        api_params["name"], name = "", api_params["name"]
        container = self._request(endpoint, **api_params)
        if not isinstance(container, dict):
            raise TypeError(f"Expected json response but received: {container}")

        # update response status to 0 or 22
        status_22 = re.findall(
            r"\((.*?)\)", container[JsonKeys.STATUS][JsonKeys.CONTENT]
        )
        if status_22:
            container[JsonKeys.STATUS][
                JsonKeys.CODE
            ] = ResponseStatus.PARTLY_MATCH.value
            container[JsonKeys.STATUS][JsonKeys.CONTENT] = status_22[0]
        else:  # i.e. status 0
            container[JsonKeys.STATUS][JsonKeys.CODE] = ResponseStatus.MATCH.value
            container[JsonKeys.STATUS][JsonKeys.CONTENT] = (
                "successfull"
                if container[JsonKeys.PARAMETER]["language"] == "en"
                else "erfolgreich"
            )
        container[JsonKeys.PARAMETER]["name"] = name

        return container

    def _get_batch_job_result(self, response: dict, wait_for_result: bool) -> dict:
        """Synchronously or asynchronously retrieve the result of a batch job.

        Parameters
        ----------
        response : dict
            The response object containing the status and content of the initial request.
            This response object is already formatted to wrapper guidelines.

        wait_for_result : bool
            If True, the method waits for the result before returning.
            If False, a thread is started to probe for the result asynchronously.
        """
        result_id = response[JsonKeys.STATUS][JsonKeys.CONTENT].split(" ")[-1]
        language = response[JsonKeys.PARAMETER]["language"]

        self.save(result_id, response)
        if wait_for_result:
            self._probe_for_result(result_id, language)
        else:
            thread = Thread(target=self._probe_for_result, args=(result_id, language))
            thread.start()
            response[JsonKeys.CONTENT] = result_id
        return self.load(result_id)

    def _probe_for_result(self, result_id: str, language: Literal["de", "en"]) -> None:
        """Probe for the result of a batch job in set time intervals.

        The response will be stored in the `_cache` attribute of the object.

        Parameters
        ----------
        result_id : str
            The unique identifier for the result.

        language : Literal['de', 'en'], default "en"
            Language the user wants the response to be in.

        Returns
        -------
        None
        """
        while True:
            result = self.result(name=result_id, language=language)
            if result[JsonKeys.STATUS][JsonKeys.CODE] == ResponseStatus.MATCH:
                self._cache[result_id][JsonKeys.CONTENT] = result[JsonKeys.CONTENT]
                self._cache[result_id][JsonKeys.STATUS] = {
                    JsonKeys.CODE: ResponseStatus.MATCH.value,
                    JsonKeys.CONTENT: "successfull"
                    if language == "en"
                    else "erfolgreich",
                    JsonKeys.TYPE: "information" if language == "en" else "Information",
                }
                return
            time.sleep(self._timeout)  # TODO: parametrize?
