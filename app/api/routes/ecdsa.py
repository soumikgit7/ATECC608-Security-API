from fastapi import APIRouter, HTTPException

from app.schemas.ecdsa_schema import SignRequest
from app.services.ecdsa import sign_data
from app.services.key_service import _key_store
from app.schemas.ecdsa_schema import SignRequest, VerifyRequest
from app.services.ecdsa import sign_data, verify_signature

router = APIRouter(
    prefix="/api/v1/ecdsa",
    tags=["ECDSA"]
)


@router.post("/sign")
def create_signature(request: SignRequest):

    key_data = _key_store.get(request.key_id)

    if key_data is None:
        raise HTTPException(
            status_code=404,
            detail="Key not found"
        )

    private_key = key_data["private_key"]

    signature = sign_data(
        private_key,
        request.data
    )

    return {
        "algorithm": "ECDSA",
        "curve": "secp256r1",
        "key_id": request.key_id,
        "signature": signature
    }
@router.post("/verify")
def verify_ecdsa_signature(request: VerifyRequest):

    key_data = _key_store.get(request.key_id)

    if key_data is None:
        raise HTTPException(
            status_code=404,
            detail="Key not found"
        )

    public_key = key_data["public_key"]

    is_valid = verify_signature(
        public_key,
        request.data,
        request.signature
    )

    return {
        "algorithm": "ECDSA",
        "key_id": request.key_id,
        "valid": is_valid
    }