from pydantic import BaseModel


class HashRequest(BaseModel):
    data: str
