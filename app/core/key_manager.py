from app.services.key_service import (
    generate_key_pair,
    get_public_key,
    _key_store
)


class KeyManager:
    """
    Manages cryptographic keys used by the Security API.

    The KeyManager provides a controlled interface for
    creating and retrieving keys without exposing the
    internal key storage directly to API routes.
    """

    @staticmethod
    def generate_key():
        """
        Generate and store a new ECC key pair.
        """
        return generate_key_pair()

    @staticmethod
    def get_key(key_id: str):
        """
        Retrieve a complete key record internally.

        This method is intended for internal cryptographic
        operations such as ECDSA and ECDH.
        """
        return _key_store.get(key_id)

    @staticmethod
    def get_public_key(key_id: str):
        """
        Retrieve only the public key information.
        """
        return get_public_key(key_id)