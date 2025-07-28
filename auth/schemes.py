from pydantic import BaseModel


class SignRequest(BaseModel):
    login: str
    password: str

