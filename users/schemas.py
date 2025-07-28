from pydantic import BaseModel


class UsersAddSchemes(BaseModel):
    name: str
    age: int
    sex: str


class UsersSchemes(UsersAddSchemes):
    id: int