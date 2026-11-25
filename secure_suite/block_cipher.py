"""Block cipher module (US1, FR1, FR2, FR15).

AES-EAX by default; DES (CBC + HMAC-SHA-256, encrypt-then-MAC) on request.
"""

import queue
import threading


def encrypt(key: bytes, data: bytes, aad: bytes = b"", cipher: str = "AES-EAX") -> bytes:
    """Return a blob containing nonce, ciphertext and tag. Fresh nonce per call."""
    # TODO: AES-EAX with fresh nonce; DES-CBC + HMAC (encrypt-then-MAC)
    raise NotImplementedError


def decrypt(key: bytes, blob: bytes, aad: bytes = b"", cipher: str = "AES-EAX") -> bytes:
    """Return plaintext; raise ValueError if authentication fails."""
    # TODO: verify tag before returning plaintext
    raise NotImplementedError


class EncryptionWorker(threading.Thread):
    """Pipeline stage: reads plaintext from in_q, writes encrypted blobs to out_q.

    Stops on a None sentinel and forwards it downstream.
    """

    def __init__(self, in_q: queue.Queue, out_q: queue.Queue, key: bytes, cipher: str = "AES-EAX"):
        super().__init__(daemon=True)
        # TODO: store queues, key and cipher
        raise NotImplementedError

    def run(self) -> None:
        # TODO: loop: get from in_q, encrypt, put to out_q; stop on None and forward it
        raise NotImplementedError
