"""Hashing and integrity module (US3, FR6, FR7, FR16)."""


def digest(data: bytes, algo: str = "SHA-256") -> bytes:
    """Return the digest of data. MD5 only on request, with a warning."""
    # TODO: SHA-256 default; MD5 only with warning
    raise NotImplementedError


def hmac_tag(key: bytes, data: bytes) -> bytes:
    """Return HMAC-SHA-256 of data under key."""
    # TODO: HMAC-SHA-256
    raise NotImplementedError


def verify_digest(data: bytes, expected: bytes, algo: str = "SHA-256") -> bool:
    """Constant-time digest comparison."""
    # TODO: use constant-time compare
    raise NotImplementedError
