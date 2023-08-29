import pytest
import requests
import responses
from genesisonline.services import BaseService
from genesisonline import exceptions
from genesisonline.constants import Endpoints, BASE_URL
from urllib.parse import urljoin
from ..conftest import (
    api_vcr,
    cassette_dir,
)

cassette_subdir = str(cassette_dir / __name__.split(".")[-1])


@pytest.fixture
def service(session):
    class ConcreteBaseService(BaseService):
        """Dummy implementation of abstract class `BaseService` for unit testing"""

        _service = ""
        endpoints = list()

        def _request(self) -> dict:
            return super()._request()

    return ConcreteBaseService(session)


@pytest.fixture
def dummy_endpoint(session):
    un, pw = session.params["username"], session.params["password"]
    url = urljoin(BASE_URL, "dummy_endpoint")
    return f"{url}?username={un}&password={pw}&language=en"


@api_vcr.use_cassette(cassette_library_dir=cassette_subdir)
def test_request(service):
    response = service.request(Endpoints.CATALOGUE_TABLES)
    assert isinstance(response, dict)


@responses.activate
def test_request_http_error(service, dummy_endpoint):
    url = urljoin(BASE_URL, "http_error")
    responses.add(responses.GET, dummy_endpoint, status=500)
    with pytest.raises(exceptions.HTTPError):
        response = service.request("dummy_endpoint")


@responses.activate
def test_request_connection_error(service, dummy_endpoint):
    url = urljoin(BASE_URL, "http_error")
    responses.add(
        responses.GET, dummy_endpoint, body=requests.exceptions.ConnectionError()
    )
    with pytest.raises(exceptions.ConnectionError):
        response = service.request("dummy_endpoint")


@responses.activate
def test_request_timeout_error(service, dummy_endpoint):
    url = urljoin(BASE_URL, "http_error")
    responses.add(responses.GET, dummy_endpoint, body=requests.exceptions.Timeout())
    with pytest.raises(exceptions.TimeoutError):
        response = service.request("dummy_endpoint")


@responses.activate
def test_request_error(service, dummy_endpoint):
    url = urljoin(BASE_URL, "http_error")
    responses.add(
        responses.GET, dummy_endpoint, body=requests.exceptions.RequestException()
    )
    with pytest.raises(exceptions.RequestError):
        response = service.request("dummy_endpoint")


@responses.activate
def test_request_unexpected_content_error(service, dummy_endpoint):
    responses.add(
        responses.GET,
        dummy_endpoint,
        body="<html></html>",
        status=200,
        content_type="text/html",
    )

    with pytest.raises(exceptions.UnexpectedContentError):
        response = service.request("dummy_endpoint")
