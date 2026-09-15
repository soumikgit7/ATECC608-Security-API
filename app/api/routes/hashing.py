from fastapi import APIRouter

from app.schemas.hash_schema import HashRequest
from app.services.hash_service import sha256_hash


router = APIRouter(
    prefix="/api/v1/hash",
    tags=["Hash"]
)


@router.post("/sha256")
def generate_sha256(request: HashRequest):

    result = sha256_hash(request.data)

    return {
        "algorithm": "SHA-256",
        "hash": result
    }