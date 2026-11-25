"""Authentication module (US5, FR11, FR12, FR13).

Salted scrypt password hashes, or self-signed certificate login.
Lock out after 5 failed attempts. Errors never say which credential was wrong.
"""


def register(username: str, password: str) -> None:
    """Create a user with a salted, slow password hash."""
    # TODO: salted scrypt hash; never store the plaintext
    raise NotImplementedError


def login(username: str, password: str) -> bool:
    """Password login with lockout and constant-time comparison."""
    # TODO: constant-time compare; lock out after 5 failures; generic errors
    raise NotImplementedError


def make_cert(name: str, private_key, public_key, valid_days: int) -> bytes:
    """Build a self-signed certificate (public key, name, expiry)."""
    # TODO: self-signed: public key, name, expiry
    raise NotImplementedError


def verify_cert(cert: bytes, challenge: bytes, signature: bytes) -> bool:
    """Check certificate signature, expiry and the signed challenge."""
    # TODO: check self-signature, expiry and signed challenge
    raise NotImplementedError
