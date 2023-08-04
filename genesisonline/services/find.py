import requests
from .base import BaseService
from ..constants import Endpoints
from ..utils import get_api_params


class FindService(BaseService):
    """Service containing methods for finding information on objects

    Objects can be tables, variables, statistics or cubes.
    """

    def __init__(self, session: requests.Session) -> None:
        super().__init__(session)

    def endpoints(self) -> list:
        return ["find"]

    def find(
        self, term: str = None, category: str = None, pagelength: str = None, **kwargs
    ) -> dict:
        """Returns lists of objects for a search (term).

        Parameters
        ----------
        term : str
            Keyword(s) to be searched. Can be any string of characters.

        category : str
            Category to be searched in.

        pagelength : str
            Maximum number of items that will be returned. Can be between 1-2500.
            defaults to 100 if `pagelength` is None.
        """
        api_params = get_api_params(locals())
        return super()._request(Endpoints.FIND_FIND, **api_params)
