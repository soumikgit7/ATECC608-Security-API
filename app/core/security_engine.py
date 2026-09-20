from app.services.key_service import generate_key_pair, get_public_key
from app.services.random_service import generate_random_bytes
from app.services.hash_service import sha256_hash
from app.services.ecdsa import sign_data, verify_signature
from app.services.ecdh import derive_shared_secret


class SecurityEngine:
    """
    Central security engine for the ATECC608 Security API.

    This class acts as a single entry point for
    cryptographic operations.
    """

    # -------------------------
    # Key Management
    # -------------------------

    @staticmethod
    def generate_key():
        return generate_key_pair()

    @staticmethod
    def get_public_key(key_id: str):
        return get_public_key(key_id)

    # -------------------------
    # Random Number Generation
    # -------------------------

    @staticmethod
    def generate_random(length: int):
        return generate_random_bytes(length)

    # -------------------------
    # SHA-256
    # -------------------------

    @staticmethod
    def hash_sha256(data: str):
        return sha256_hash(data)

    # -------------------------
    # ECDSA
    # -------------------------

    @staticmethod
    def sign(private_key, data: str):
        return sign_data(private_key, data)

    @staticmethod
    def verify(public_key, data: str, signature: str):
        return verify_signature(
            public_key,
            data,
            signature
        )

    # -------------------------
    # ECDH
    # -------------------------

    @staticmethod
    def derive_secret(private_key, peer_public_key):
        return derive_shared_secret(
            private_key,
            peer_public_key
        )