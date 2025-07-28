from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from base.connection_settings import settings
from base.base_model import Base



engine = create_async_engine(settings.db_url, echo=False)
SessionMaker = async_sessionmaker(engine, expire_on_commit=False)


async def _db_init() -> None:
    async with engine.begin() as conn:
        #await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)



async def get_db():
    async with SessionMaker() as session:
        yield session




