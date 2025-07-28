from sqlalchemy.ext.asyncio import AsyncSession
from users.models import Posts
from base.base_crud import CRUD



class PostsCRUD(CRUD):
    def __init__(self, session: AsyncSession):
        super().__init__(table=Posts, session=session)
