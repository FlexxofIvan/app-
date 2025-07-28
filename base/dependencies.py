from typing import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from base.database import get_db
from fastapi import Depends


SessionDep = Annotated[AsyncSession, Depends(get_db)]