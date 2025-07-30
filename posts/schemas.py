from pydantic import BaseModel
import datetime


class PostsAddSchemes(BaseModel):
    text: str


class PostsSchemes(PostsAddSchemes):
    id: int
    author: str
    #time: datetime


class PostResponseSchema(BaseModel):
    message: str