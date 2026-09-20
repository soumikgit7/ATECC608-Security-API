from pydantic import BaseModel


class SignRequest(BaseModel):
    key_id: str
    data: str
class VerifyRequest(BaseModel):
    key_id: str
    data: str
    signature: str