from sqlalchemy.ext.asyncio import AsyncSession
from users.models import Posts
from base.base_crud import CRUD



class PostsCRUD(CRUD):
    def __init__(self, session: AsyncSession):
        super().__init__(table=Posts, session=session)

    async def change_text(self, idx: int, text: str):
        post = await self.session.get(self.table, idx)
        if post:
            post.text = text
            await self.session.commit()
            await self.session.refresh(post)
            return post
        else:
            return None