from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert

from src.database.database import get_async_session
from .models import Anime
from .schemas import NewAnimeCreate

from src.comment.models import Comment

router_anime = APIRouter(
    prefix="/anime",
    tags=["anime"]
)


'''@router_anime.get('/{anime_id}')
async def get_anime(Anime_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Anime).filter(Anime.id == Anime_id)
    if query is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    result = await session.execute(query)
    return result.scalars().all()'''


@router_anime.get('/{anime_id}')
async def get_anime(Anime_id: int, session: AsyncSession = Depends(get_async_session)):
    query = select(Anime).filter(Anime.id == Anime_id).filter(Comment.anime_id == Anime_id)
    if query is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    result = await session.execute(query)
    return result.scalars().all()


@router_anime.post('/add_anime')
async def add_anime(new_anime: NewAnimeCreate, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Anime).values(**new_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "success"}