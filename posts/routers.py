from fastapi import APIRouter
from fastapi import HTTPException, status
from posts.schemas import PostsAddSchemes, PostResponseSchema
from users.dependencies import UserDep
from posts.transactions import PostsCRUD
from base.dependencies import SessionDep

post_router = APIRouter(
        tags=['posts']
)

@post_router.post('/', status_code=status.HTTP_201_CREATED)
async def create_post(comment: PostsAddSchemes, session: SessionDep, user: UserDep):
    post_text = comment.text
    author_id = user.id

    if post_text and author_id:
        crud = PostsCRUD(session=session)
        data = {"text": post_text, "author_id": author_id}
        post = await crud.create(data)
        return {"message": "created!",
                "id": post.id
                }
    return {"error": "Invalid post data or author"}


@post_router.get('/')
async def get_all(session: SessionDep):
    crud = PostsCRUD(session=session)
    results = await crud.read_all()
    if not results:
        return {"message": "No posts found", "posts": []}
    else:
        return results


@post_router.delete('/{post_id}')
async def delete_post(post_id: int, session: SessionDep, user: UserDep):
    crud = PostsCRUD(session=session)
    post = await crud.get(post_id)

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Post not found"
        )

    accession_rule = (post.author.id == user.id)
    if not accession_rule:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail="You do not have permission to delete this post.")
    else:
        await crud.delete(post)
        return {"mess": "deleted"}


@post_router.patch('/{post_id}')
async def change_post(post_id: int, post_resp: PostResponseSchema, session: SessionDep, user: UserDep):
    crud = PostsCRUD(session=session)
    post = await crud.get(id=post_id)

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    else:
        accession_rule = (post.author_id == user.id)
        if not accession_rule:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                                detail="You do not have permission to delete this post.")
        else:
            result = await crud.change_text(text=post_resp.message, idx=post_id)
            if result:
                return HTTPException(status_code=status.HTTP_204_NO_CONTENT)


