from typing import Any, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import delete, select, update, exists, and_


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

    async def read_all(self):
        stmt = select(self.table)
        result = await self.session.execute(stmt)
        records = result.scalars().all()
        return records

    async def delete_by_filter(self, filt: Any) -> int:
        condition = filt if not isinstance(filt, (list, tuple)) else and_(*filt)
        stmt = delete(self.table).where(condition)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount

    async def read_by_filter(self, filt: Any) -> Optional[list]:
        condition = filt if not isinstance(filt, (list, tuple)) else and_(*filt)
        stmt = select(self.table).where(condition)
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get(self, id: int) -> DeclarativeBase:
        return await self.session.get(self.table, id)

    async def delete(self, obj):
        await self.session.delete(obj)
        await self.session.commit()

    async def update_by_filter(self, new_vals: dict, filt: Any) -> int:
        condition = filt if not isinstance(filt, (list, tuple)) else and_(*filt)
        stmt = update(self.table).where(condition).values(**new_vals)
        result = await self.session.execute(stmt)
        await self.session.commit()
        return result.rowcount

    async def check_by_filter(self, filt: Any) -> bool:
        condition = filt if not isinstance(filt, (list, tuple)) else and_(*filt)
        stmt = select(exists().where(condition)).select_from(self.table)
        result = await self.session.execute(stmt)
        return result.scalars().one()

