# Secure Communication Suite

CSE461 Cryptography and Security, Fall 2026. A Python secure chat over TCP (loopback) built from a queue pipeline of worker threads.

**Status:** Phase 1 (design). The code is a skeleton: every function raises `NotImplementedError` and has a `TODO`.

## Modules

| File | Purpose |
| --- | --- |
| `block_cipher.py` | AES-EAX / DES encryption, `EncryptionWorker` |
| `public_key.py` | RSA / ECC, key wrapping, signatures |
| `hashing.py` | SHA-256 / MD5, HMAC |
| `key_management.py` | Key store, session keys, key derivation |
| `auth.py` | Password and certificate login |
| `secure_chat.py` | TCP server and client |
| `pipeline.py` | Send and receive worker pipelines |
| `main.py` | CLI menu and `--demo` |
| `config.py` | Algorithm selection and defaults |

## Setup

```powershell
pip install -r secure_suite/requirements.txt
python -m unittest discover -s secure_suite/tests -t .
```

Defaults are AES-EAX, RSA-2048, SHA-256 and password auth. DES and MD5 are broken and only available behind an explicit flag.

## Docs

Plan, SRS and design: `Secure Communication Suite Phase 1 Design and Planning.md`.
