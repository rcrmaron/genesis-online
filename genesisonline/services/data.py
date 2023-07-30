import requests
from .base import BaseService
from ..constants import Endpoints


class DataService(BaseService):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return ["chart2result", "result"]

    def chart2result(self, **kwargs) -> dict:
        return super()._request("data_chart2result", params=kwargs)

    def result(self, **kwargs) -> dict:
        return super()._request("data_result", params=kwargs)
