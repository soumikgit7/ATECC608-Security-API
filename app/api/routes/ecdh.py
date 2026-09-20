from fastapi import APIRouter, HTTPException

from app.schemas.ecdh_schema import ECDHRequest
from app.services.ecdh import derive_shared_secret
from app.services.key_service import _key_store


router = APIRouter(
    prefix="/api/v1/ecdh",
    tags=["ECDH"]
)


@router.post("/derive")
def derive_ecdh_secret(request: ECDHRequest):

    private_key_data = _key_store.get(
        request.private_key_id
    )

    if private_key_data is None:
        raise HTTPException(
            status_code=404,
            detail="Private key not found"
        )

    peer_key_data = _key_store.get(
        request.peer_key_id
    )

    if peer_key_data is None:
        raise HTTPException(
            status_code=404,
            detail="Peer key not found"
        )

    private_key = private_key_data["private_key"]
    peer_public_key = peer_key_data["public_key"]

    shared_secret = derive_shared_secret(
        private_key,
        peer_public_key
    )

    return {
        "algorithm": "ECDH",
        "curve": "secp256r1",
        "shared_secret": shared_secret
    }