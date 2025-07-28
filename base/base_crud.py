from typing import Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import delete, select, update


class CRUD:
    def __init__(self, table: DeclarativeBase, session: AsyncSession):
        self.session = session
        self.table = table

    async def create(self, data: dict) -> DeclarativeBase:
        new = self.table(**data)
        self.session.add(new)
        await self.session.commit()
        await self.session.refresh(new)
        return new

    async def delete_by_filter(self, filt: Any) -> int:
        stmt = delete(self.table).where(*filt)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount

    async def read_by_filter(self, filt: Any) -> Optional[list]:
        stmt = select(self.table).where(*filt)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def update_by_filter(self, new_vals: dict, filt: Any) -> int:
        stmt = update(self.table).where(*filt).values(**new_vals)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount
