
import hashlib
import secrets

# Temporary in-memory API key store
# Later this will be replaced with a database.
_api_key_store = {}


def _hash_api_key(api_key: str) -> str:
    """
    Hash an API key using SHA-256.
    """
    return hashlib.sha256(
        api_key.encode("utf-8")
    ).hexdigest()


def generate_api_key():
    """
    Generate a new API key.

    The raw API key is returned only once.
    Only its hash is stored internally.
    """

    api_key = "sk_live_" + secrets.token_urlsafe(32)

    key_id = secrets.token_hex(8)

    key_hash = _hash_api_key(api_key)

    _api_key_store[key_hash] = {
        "key_id": key_id,
        "active": True
    }

    return {
        "key_id": key_id,
        "api_key": api_key
    }


def verify_api_key(api_key: str) -> bool:
    """
    Verify whether an API key exists and is active.
    """

    key_hash = _hash_api_key(api_key)

    key_data = _api_key_store.get(key_hash)

    if key_data is None:
        return False

    return key_data["active"]
