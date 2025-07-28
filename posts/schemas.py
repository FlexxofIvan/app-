from pydantic import BaseModel
import datetime


class PostsAddSchemes(BaseModel):
    post: str


class PostsSchemes(PostsAddSchemes):
    id: int
    author: str
    #time: datetime