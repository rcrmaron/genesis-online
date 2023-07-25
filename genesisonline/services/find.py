import requests
from typing import Literal
from .base import BaseService


class FindService(BaseService):
    def __init__(
        self,
        session: requests.Session,
        username: str,
        password: str,
        language: Literal["de", "en"] = "en",
    ) -> None:
        super().__init__(session, username, password, language)

    def endpoints(self) -> list:
        return ["find"]

    def find(
        self, term: str = None, category: str = None, pagelength: str = None, **kwargs
    ) -> dict:
        return super()._request(
            "find_find", term=term, category=category, pagelength=pagelength, **kwargs
        )
