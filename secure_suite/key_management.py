"""Key management module (US4, FR8, FR9, FR10)."""


class KeyStore:
    """Stores private keys encrypted at rest under a scrypt-derived password key.

    Session keys are held in memory only and wiped when the session ends.
    """

    def __init__(self, path: str):
        # TODO: load or create the key file at path
        raise NotImplementedError

    def save_private_key(self, name: str, key_bytes: bytes, password: str) -> None:
        # TODO: encrypt under scrypt-derived key before writing
        raise NotImplementedError

    def load_private_key(self, name: str, password: str) -> bytes:
        # TODO: derive key from password, decrypt
        raise NotImplementedError

    def add_session_key(self, session_id: str, key: bytes) -> None:
        # TODO: keep in memory only
        raise NotImplementedError

    def get_session_key(self, session_id: str) -> bytes:
        # TODO: raise KeyError if the session is unknown
        raise NotImplementedError

    def end_session(self, session_id: str) -> None:
        """Wipe and discard the session's keys."""
        # TODO: overwrite key bytes, then delete
        raise NotImplementedError


def new_session_key(length: int = 32) -> bytes:
    """Random key from the OS secure source."""
    # TODO: use the OS random source
    raise NotImplementedError


def derive_keys(secret: bytes, client_nonce: bytes, server_nonce: bytes) -> tuple[bytes, bytes]:
    """Derive (encryption_key, mac_key) from a shared secret and both nonces."""
    # TODO: KDF over secret + both nonces; split into enc and MAC keys
    raise NotImplementedError
