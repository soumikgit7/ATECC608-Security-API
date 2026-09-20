from fastapi import APIRouter, HTTPException

from app.core.key_manager import KeyManager

router = APIRouter(
    prefix="/api/v1/keys",
    tags=["Keys"]
)


@router.post("/generate")
def generate_keys():
    return KeyManager.generate_key()


@router.get("/{key_id}")
def retrieve_public_key(key_id: str):

    key_data = KeyManager.get_public_key(key_id)

    if key_data is None:
        raise HTTPException(
            status_code=404,
            detail="Key not found"
        )

    return key_data