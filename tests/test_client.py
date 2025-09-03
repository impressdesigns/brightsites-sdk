"""Testing the client."""

from brightsites_sdk import BrightsitesServices


def test_smoke() -> None:
    """Temporary test to check if the tests are running."""
    client = BrightsitesServices(
        base_url="https://subdomain.mybrightsites.com/api/v2.6.1",
        username="",
        password="",
        timeout=10.0,
    )
    assert client is not None
