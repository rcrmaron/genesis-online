import requests
from .base import BaseService
from ..constants import Endpoints


class FindService(BaseService):
    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return ["find"]

    def find(
        self, term: str = None, category: str = None, pagelength: str = None, **kwargs
    ) -> dict:
        return super()._request(
            Endpoints.FIND_FIND,
            term=term,
            category=category,
            pagelength=pagelength,
            **kwargs
        )
