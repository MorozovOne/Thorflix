from typing import AsyncGenerator
from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base

from .config import get_settings

db_user = get_settings().get('db_user')
db_pass = get_settings().get('db_pass')
db_host = get_settings().get('db_host')
db_name = get_settings().get('db_pass')

database_url = f"postgresql+asyncpg://{db_user}:{db_pass}@{db_host}:5432/{db_name}"

async_engine = create_async_engine(database_url)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

Base = declarative_base()

metadata = MetaData()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session