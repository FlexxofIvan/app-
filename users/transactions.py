from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from users.models import Users
from base.base_crud import CRUD



class UsersCRUD(CRUD):
    def __init__(self, session: AsyncSession):
        super().__init__(table=Users, session=session)

    async def get_new_posts(self,
                        id : int
                        ) -> Optional[list]:
        stm = (select(self.table.new_posts)
               .where(self.table.id == id)
               )
        result = await self.session.execute(stm)
        return result.scalars().all()



