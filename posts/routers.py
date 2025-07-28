from fastapi import APIRouter, status

from posts.schemas import PostsAddSchemes
from users.dependencies import UserDep
from base.base_crud import CRUD
from posts.models import Posts
from base.dependencies import SessionDep

post_router = APIRouter(
        tags=['posts']
)

@post_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_post(comment: PostsAddSchemes, session: SessionDep, user: UserDep):
    post_text = comment.post
    author_id = user.id

    if post_text and author_id:
        post_crud = CRUD(session=session, table=Posts)
        data = {"post": post_text, "author_id": author_id}
        await post_crud.create(data)
        return {"message": "created!"}

    return {"error": "Invalid post data or author"}