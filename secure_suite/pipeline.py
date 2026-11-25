"""Worker-thread pipelines joined by queues (FR13, FR15, NFR3).

Send: hash -> encrypt -> sign.  Receive: verify -> decrypt -> check hash.
Every stage stops on a None sentinel and passes it on.
"""

from .config import SuiteConfig


class SendPipeline:
    def __init__(self, config: SuiteConfig, keys):
        # TODO: create queues and start the worker threads
        raise NotImplementedError

    def submit(self, user: str, message: bytes) -> None:
        """Accept a message only for authenticated users."""
        # TODO: reject unauthenticated users (FR13)
        raise NotImplementedError

    def get(self) -> bytes:
        # TODO: block on the output queue
        raise NotImplementedError

    def shutdown(self) -> None:
        # TODO: send None sentinel and join workers
        raise NotImplementedError


class ReceivePipeline:
    def __init__(self, config: SuiteConfig, keys):
        # TODO: create queues and start the worker threads
        raise NotImplementedError

    def submit(self, frame: bytes) -> None:
        # TODO: queue the frame for verification
        raise NotImplementedError

    def get(self) -> bytes:
        """Return plaintext, or raise if the message is flagged as tampered."""
        # TODO: block on the output queue
        raise NotImplementedError

    def shutdown(self) -> None:
        # TODO: send None sentinel and join workers
        raise NotImplementedError
