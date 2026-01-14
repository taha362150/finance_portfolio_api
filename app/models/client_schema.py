from pydantic import BaseModel

class ClientOut(BaseModel):
    client_id: int
    name: str
    email: str