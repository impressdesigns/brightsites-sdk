"""Brightsites API client."""

from typing import Any

from httpx import Client, Response

from .models import OrdersList


class BrightsitesServices:
    """A class wrapping Brightsites interaction."""

    def __init__(
        self,
        base_url: str,
        token: str,
        timeout: float = 10.0,
    ) -> None:
        """Initialize the BrightsitesServices class."""
        self.client = Client(
            base_url=base_url,
            params={"token": token},
            timeout=timeout,
        )

    def _make_request(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None = None,
        json: dict[str, Any] | None = None,
    ) -> Response:
        """Make a request to Brightsites."""
        args: dict[str, str | dict[str, str]] = {
            "url": path,
            "method": method,
        }

        if params is not None:
            args["params"] = params

        if json is not None:
            args["json"] = json

        return self.client.request(**args)  # type: ignore[arg-type]

    def list_orders(self) -> OrdersList:
        """List the orders."""
        response = self._make_request(
            method="GET",
            path="/orders",
        )
        response.raise_for_status()
        return OrdersList.model_validate(response.json())
