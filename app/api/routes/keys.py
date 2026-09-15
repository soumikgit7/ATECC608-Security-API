from fastapi import APIRouter

from app.services.key_service import generate_key_pair


router = APIRouter(
    prefix="/api/v1/keys",
    tags=["Keys"]
)


@router.post("/generate")
def generate_keys():
    return generate_key_pair()
    return {
        "message": "Key pair generated successfully"
    }