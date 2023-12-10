from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from animes.schemas import AnimeSchema
from database import get_async_session
from models import Anime, Comment

router_anime = APIRouter(
    prefix="/animes",
    tags=["animes"]
)



@router_anime.get("/get_anime/{anime_id}")
async def get_anime(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Anime).options(selectinload(Anime.comment)).filter(Anime.id == anime_id)
    result = await session.execute(query)
    anime = result.scalars().first()

    if anime is None:
        raise HTTPException(status_code=404, detail="Anime not found")

    return anime



@router_anime.post('/add_anime', response_model=None)
async def add_anime(new_anime: AnimeSchema, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Anime).values(**new_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}

