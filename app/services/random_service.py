import secrets
def generate_random_bytes(length: int):
    """
    Generate cryptographically secure random bytes.
    """
    random_data = secrets.token_bytes(length)
    return random_data.hex()