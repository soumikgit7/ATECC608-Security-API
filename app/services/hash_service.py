import hashlib


def sha256_hash(data: str) -> str:
    """
    Generate a SHA-256 hash from input data.
    """

    hash_object = hashlib.sha256(
        data.encode("utf-8")
    )

    return hash_object.hexdigest()