"""Secure chat over TCP on loopback (US6, FR14).

Handshake: hello -> server key + signature -> pinned-fingerprint check and
key exchange -> derive keys -> credentials in the encrypted channel -> ok/denied.
Frames: sequence number, nonce, ciphertext, tag.
"""


class ChatServer:
    def __init__(self, host: str = "127.0.0.1", port: int = 0):
        # TODO: bind or store address
        raise NotImplementedError

    def start(self) -> None:
        # TODO: accept loop; run the 7-step handshake per connection
        raise NotImplementedError

    def stop(self) -> None:
        # TODO: close the socket and join threads
        raise NotImplementedError


class ChatClient:
    def __init__(self, host: str, port: int, server_fingerprint: bytes):
        # TODO: store server address and pinned fingerprint
        raise NotImplementedError

    def connect(self, username: str, password: str) -> bool:
        """Run the handshake and authenticate."""
        # TODO: handshake: hello, pin server fingerprint, key exchange, credentials
        raise NotImplementedError

    def send(self, message: str) -> None:
        # TODO: frame = seq, nonce, ciphertext, tag
        raise NotImplementedError

    def receive(self) -> str:
        # TODO: reject replayed, reordered or altered frames
        raise NotImplementedError

    def close(self) -> None:
        # TODO: end session and wipe keys
        raise NotImplementedError
