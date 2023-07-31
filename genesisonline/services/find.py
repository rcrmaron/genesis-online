import requests
from .base import BaseService
from ..constants import Endpoints
from ..utils import get_api_params


class FindService(BaseService):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return ["find"]

    def find(
        self, term: str = None, category: str = None, pagelength: str = None, **kwargs
    ) -> dict:
        api_params = get_api_params(locals())
        return super()._request(Endpoints.FIND_FIND, **api_params)
