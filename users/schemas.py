from typing import Optional

from pydantic import BaseModel


class UsersAddSchemes(BaseModel):
    name: str
    age: int
    sex: str


class UsersPatchSchemes(BaseModel):
    name: Optional[str]
    age: Optional[int]
    sex: Optional[str]
    password: Optional[str]


class UsersSchemes(UsersAddSchemes):
    id: int


class UsersPutSchemes(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    password: str