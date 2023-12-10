import asyncio

from sqlalchemy import Integer, and_, cast, func, insert, inspect, or_, select, text
from sqlalchemy.orm import aliased, contains_eager, joinedload, selectinload

from database import Base, engine, get_async_session

from models import Anime

class AsyncORM:
    @staticmethod
    async def create_tables():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def insert_anime():
        async with get_async_session() as session:
            Anime_name = Anime(name="Jack")
            Poster = Anime(poster="image.png")
            session.add_all([Anime_name, Poster])
            await session.flush()
            await session.commit()

    asyncio.run(create_tables())