"""Functionality for interacting with the GENESIS-Online Data service.
"""
import requests
import time
import re
import logging
from threading import Thread
from typing import Union
from pathlib import Path
from genesisonline.services.base import BaseService
from genesisonline.constants import Endpoints, ResponseStatus, JsonKeys
from genesisonline.exceptions import StandardizationError
from genesisonline.filemanager import FileManager

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal

logger = logging.getLogger(__name__)


class DataService(BaseService):
    """Service containing methods for downloading data.

    This class offers methods to retrieve various data-related information,
    including charts, cubes, maps, and more, from the GENESIS-Online database.

    This service does not implement the following endpoints as they are
    redundant (due to the way responses are standardized here):<br>
    - cubefile (call `cube` instead)<br>
    - resultfile (call `result` instead)<br>
    - tablefile (call `table` instead)<br>
    - timeseriesfile (call `timeseries` instead)
    """

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

    def __init__(
        self, session: requests.Session, cache: Union[Path, str] = None
    ) -> None:
        """
        Args:
            cache: path to where the results of large table operations are saved.
                If `None`, results are stored in the user's home directory.
        """
        super().__init__(session)
        self._timeout = 30
        self.filemanager = FileManager(cache)

    def __str__(self) -> str:
        return "Service containing methods for downloading data."

    def load(self, result_id):
        file_name = f"{result_id}.json"
        return self.filemanager.load(file_name)

    def save(self, object, result_id):
        file_name = f"{result_id}.json"
        self.filemanager.save(object, file_name)

    def chart2result(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns a chart related to results table `name` from `area`."""
        return self._request(
            Endpoints.DATA_CHART2RESULT, name=name, area=area, **api_params
        )

    def chart2table(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns a chart related to table `name` from `area`."""
        return self._request(
            Endpoints.DATA_CHART2TABLE, name=name, area=area, **api_params
        )

    def chart2timeseries(
        self, name: str = None, area: str = None, **api_params
    ) -> dict:
        """Returns a chart related to timeseries `name` from `area`."""
        return self._request(
            Endpoints.DATA_CHART2TIMESERIES, name=name, area=area, **api_params
        )

    def cube(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns cube `name` from `area` according to the parameters set."""
        return self._request(Endpoints.DATA_CUBE, name=name, area=area, **api_params)

    def map2result(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns a map related to results table `name` from `area`."""
        return self._request(
            Endpoints.DATA_MAP2RESULT, name=name, area=area, **api_params
        )

    def map2table(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns a map related to table `name` from `area`."""
        return self._request(
            Endpoints.DATA_MAP2TABLE, name=name, area=area, **api_params
        )

    def map2timeseries(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns a map related to timeseries `name` from `area`."""
        return self._request(
            Endpoints.DATA_MAP2TIMESERIES, name=name, area=area, **api_params
        )

    def result(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns results table `name` from `area` according to the parameters set."""
        return self._request(Endpoints.DATA_RESULT, name=name, area=area, **api_params)

    def table(
        self,
        wait_for_result: bool = True,
        name: str = None,
        area: str = None,
        **api_params,
    ) -> dict:
        """Returns table `name` from `area`according to the parameters set.

        Async if `wait_for_result` = False.
        """
        response = self._request(
            Endpoints.DATA_TABLE, name=name, area=area, job="true", **api_params
        )

        if response[JsonKeys.STATUS][JsonKeys.CODE] == ResponseStatus.BACKGROUND_RUN:
            return self._get_batch_job_result(response, wait_for_result)
        return response

    def timeseries(self, name: str = None, area: str = None, **api_params) -> dict:
        """Returns timeseries `name` from `area` according to the parameters set."""
        return self._request(
            Endpoints.DATA_TIMESERIES, name=name, area=area, **api_params
        )

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
        """Standaridze response according to wrapper guidelines."""
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

        Note that the intermediate and final results are always saved to disk
        as a json file (as they can be quite large?).

        Args:
            response: the response object containing the status and content of
                the initial request. This response object is already formatted
                to wrapper guidelines.
            wait_for_result: if True, the method waits for the result before
                returning. If False, a thread is started to probe for the
                result asynchronously.
        """
        result_id = response[JsonKeys.STATUS][JsonKeys.CONTENT].split(" ")[-1]
        language = response[JsonKeys.PARAMETER]["language"]

        self.save(response, result_id)
        if wait_for_result:
            self._probe_for_result(result_id, language)
        else:
            thread = Thread(target=self._probe_for_result, args=(result_id, language))
            thread.start()
            response[JsonKeys.CONTENT] = result_id
            self.save(response, result_id)

        # load results as batch jobs are always saved as file
        return self.load(result_id)

    def _probe_for_result(self, result_id: str, language: Literal["de", "en"]) -> None:
        """Probe for the result of a batch job in set time intervals.

        The response will be stored as a json file.

        Args:
            result_id: the unique identifier for the result.
            language: language the user wants the response to be in.
        """
        while True:
            logger.info(
                f"Checking for result '{result_id}' every {self._timeout} second(s)."
            )
            result = self.result(name=result_id, language=language)
            if result[JsonKeys.STATUS][JsonKeys.CODE] == ResponseStatus.MATCH:
                primary_result = self.load(result_id)
                primary_result[JsonKeys.CONTENT] = result[JsonKeys.CONTENT]
                primary_result[JsonKeys.STATUS] = {
                    JsonKeys.CODE: ResponseStatus.MATCH.value,
                    JsonKeys.CONTENT: "successfull"
                    if language == "en"
                    else "erfolgreich",
                    JsonKeys.TYPE: "information" if language == "en" else "Information",
                }
                self.save(primary_result, result_id)
                return
            time.sleep(self._timeout)  # TODO: parametrize?
