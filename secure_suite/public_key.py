"""Public-key module (US2, FR3, FR4, FR5).

RSA-2048 (OAEP, PSS) or ECC P-256 (ECDH, ECDSA).
"""


def generate_keypair(kind: str = "RSA"):
    """Return (private_key, public_key) for kind 'RSA' or 'ECC'."""
    # TODO: RSA-2048 or ECC P-256
    raise NotImplementedError


def wrap_key(public_key, session_key: bytes) -> bytes:
    """Wrap a session key for the partner (RSA-OAEP, or ECDH + SHA-256 KDF)."""
    # TODO: RSA-OAEP, or ECDH + SHA-256 KDF
    raise NotImplementedError


def unwrap_key(private_key, wrapped: bytes) -> bytes:
    """Recover a session key wrapped with wrap_key."""
    # TODO: inverse of wrap_key
    raise NotImplementedError


def sign(private_key, message: bytes) -> bytes:
    """Sign a message (RSA-PSS or ECDSA)."""
    # TODO: RSA-PSS or ECDSA
    raise NotImplementedError


def verify(public_key, message: bytes, signature: bytes) -> bool:
    """Return True only if the signature is valid."""
    # TODO: return False on bad signature, never raise
    raise NotImplementedError
