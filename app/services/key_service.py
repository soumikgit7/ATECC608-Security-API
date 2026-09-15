import uuid

from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    PublicFormat
)


# Temporary in-memory key store
_key_store = {}


def generate_key_pair():
    """
    Generate an ECC key pair and store it internally.
    """

    # Generate private key
    private_key = ec.generate_private_key(
        ec.SECP256R1()
    )

    # Generate corresponding public key
    public_key = private_key.public_key()

    # Generate unique identifier for this key pair
    key_id = str(uuid.uuid4())

    # Store the key pair internally
    _key_store[key_id] = {
        "private_key": private_key,
        "public_key": public_key
    }

    # Convert public key to bytes for API response
    public_key_bytes = public_key.public_bytes(
        encoding=Encoding.PEM,
        format=PublicFormat.SubjectPublicKeyInfo
    )

    return {
        "key_id": key_id,
        "algorithm": "ECC",
        "curve": "secp256r1",
        "public_key": public_key_bytes.decode("utf-8")
    }