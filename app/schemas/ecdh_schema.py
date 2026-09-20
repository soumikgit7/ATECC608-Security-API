from pydantic import BaseModel


class ECDHRequest(BaseModel):
    private_key_id: str
    peer_key_id: str