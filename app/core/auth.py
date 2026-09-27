from fastapi import HTTPException, Security
from fastapi.security import APIKeyHeader

from app.core.api_key import verify_api_key


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False
)


def require_api_key(
    api_key: str | None = Security(api_key_header)
):
    """
    Require a valid API key for protected endpoints.
    """

    if not api_key:
        raise HTTPException(
            status_code=401,
            detail="Missing API key"
        )

    if not verify_api_key(api_key):
        raise HTTPException(
            status_code=401,
            detail="Invalid API key"
        )

    return api_key
