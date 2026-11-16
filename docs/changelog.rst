Changelog
=========

- :feature:`-` Switch the HTTP client from httpx to niquests. **Breaking:** the client's ``client`` attribute
  is now ``session``, and a failed request raises :class:`niquests.HTTPError`
- :support:`-` Require Python 3.14, the floor the other Impress Designs SDKs already share

- :release:`0.2.0 <22nd October 2025>`
- :feature:`-` Add page parameter to list products

- :release:`0.1.1 <22nd October 2025>`
- :bug:`-` Fix types for some nullable fields

- :release:`0.1.0 <3rd September 2025>`
- :feature:`-` Initial release
