"""Testing the client."""

from brightsites_sdk import BrightsitesServices


def test_smoke() -> None:
    """Temporary test to check if the tests are running."""
    client = BrightsitesServices(
        base_url="https://subdomain.mybrightsites.com/api/v2.6.1",
        token="hi",  # noqa: S106 -- junk value for tests
    )
    assert client is not None
