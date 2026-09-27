
from fastapi import APIRouter

from app.core.api_key import generate_api_key


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post("/api-key")
def create_api_key():
    """
    Generate a new API key.

    The API key should be saved by the client because
    the raw key is not stored by the server.
    """

    return generate_api_key()
