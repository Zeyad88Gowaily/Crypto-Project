"""Algorithm selection and defaults (FR1, FR3, FR6, FR12, FR16).

Defaults are the secure ones. DES and MD5 require an explicit opt-in flag.
"""

from dataclasses import dataclass

SYMMETRIC_CIPHERS = ("AES-EAX", "DES")
PUBLIC_KEY_KINDS = ("RSA", "ECC")
HASH_ALGORITHMS = ("SHA-256", "MD5")
AUTH_MODES = ("password", "certificate")

MAX_FAILED_LOGINS = 5


@dataclass
class SuiteConfig:
    """Selected algorithms for one suite instance."""

    cipher: str = "AES-EAX"
    aes_key_bits: int = 256
    public_key: str = "RSA"
    rsa_bits: int = 2048
    hash_algo: str = "SHA-256"
    auth_mode: str = "password"
    allow_weak: bool = False  # must be True to use DES or MD5


def validate(config: SuiteConfig) -> None:
    """Raise ValueError for unsupported choices; warn if DES or MD5 selected."""
    # TODO: check cipher/hash/auth choices; require allow_weak for DES/MD5
    raise NotImplementedError


def warn_if_weak(config: SuiteConfig) -> None:
    """Show the DES/MD5 warning (FR16)."""
    # TODO: print warning when DES or MD5 is selected
    raise NotImplementedError
