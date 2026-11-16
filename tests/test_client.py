"""Tests for the Brightsites client."""

import json
from typing import Any

import pytest
from niquests import HTTPError, Response

from brightsites_sdk import BrightsitesServices

PAGE: dict[str, Any] = {"meta": {"total": 0, "offset": 0, "limit": 50}}


def _response(status_code: int, body: dict[str, Any] | None = None) -> Response:
    """Build a niquests Response without touching the network."""
    response = Response()
    response.status_code = status_code
    response._content = json.dumps(body or {}).encode()  # noqa: SLF001 -- no public way to seed a canned body
    return response


class _SessionRecorder:
    """Stand-in for ``Session.request`` serving canned responses and recording calls."""

    def __init__(self, responses: list[Response]) -> None:
        self.responses = responses
        self.calls: list[dict[str, Any]] = []

    def request(self, **kwargs: Any) -> Response:  # noqa: ANN401 -- mirrors Session.request's open signature
        self.calls.append(kwargs)
        return self.responses.pop(0)


@pytest.fixture
def client() -> BrightsitesServices:
    """Build a client for a store that is never reached."""
    return BrightsitesServices(
        base_url="https://subdomain.mybrightsites.com/api/v2.6.1",
        token="hi",  # noqa: S106 -- junk value for tests
    )


def test_session_sends_the_token_with_every_request(client: BrightsitesServices) -> None:
    """The store's token rides along as a query parameter."""
    assert client.session.params == {"token": "hi"}
    assert client.session.base_url == "https://subdomain.mybrightsites.com/api/v2.6.1"


def test_list_products_asks_for_the_page(client: BrightsitesServices, monkeypatch: pytest.MonkeyPatch) -> None:
    """Listing products names the page it wants."""
    recorder = _SessionRecorder([_response(200, {**PAGE, "products": []})])
    monkeypatch.setattr(client.session, "request", recorder.request)

    products = client.list_products(page=3)

    assert recorder.calls == [{"url": "/products", "method": "GET", "params": {"page": 3}}]
    assert products.products == []


def test_a_refused_request_raises(client: BrightsitesServices, monkeypatch: pytest.MonkeyPatch) -> None:
    """An error status surfaces as an exception instead of an empty result."""
    recorder = _SessionRecorder([_response(401)])
    monkeypatch.setattr(client.session, "request", recorder.request)

    with pytest.raises(HTTPError):
        client.list_orders()
