from cryptography.hazmat.primitives.asymmetric import ec


def derive_shared_secret(private_key, peer_public_key) -> str:
    """
    Derive a shared secret using ECDH.
    """

    shared_secret = private_key.exchange(
        ec.ECDH(),
        peer_public_key
    )

    return shared_secret.hex()