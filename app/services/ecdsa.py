from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec

from cryptography.exceptions import InvalidSignature


def verify_signature(public_key, data: str, signature_hex: str) -> bool:
    """
    Verify an ECDSA signature.
    """

    try:
        signature = bytes.fromhex(signature_hex)

        public_key.verify(
            signature,
            data.encode("utf-8"),
            ec.ECDSA(hashes.SHA256())
        )

        return True

    except InvalidSignature:
        return False
def sign_data(private_key, data: str) -> str:
    """
    Generate an ECDSA signature for the given data.
    """

    signature = private_key.sign(
        data.encode("utf-8"),
        ec.ECDSA(hashes.SHA256())
    )

    return signature.hex()