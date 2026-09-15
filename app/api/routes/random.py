from fastapi import APIRouter, HTTPException

from app.services.random_service import generate_random_bytes


router = APIRouter(
    prefix="/api/v1/random",
    tags=["Random"]
)


@router.post("/generate")
def generate_random(length: int = 32):

    if length <= 0:
        raise HTTPException(
            status_code=400,
            detail="Length must be greater than 0"
        )

    if length > 1024:
        raise HTTPException(
            status_code=400,
            detail="Length cannot exceed 1024 bytes"
        )

    random_data = generate_random_bytes(length)

    return {
        "length": length,
        "random_data": random_data
    }