from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload, Load, subqueryload, joinedload, load_only

from animes.schemas import CreateAnime, ReadAnime
from database import get_async_session
from models import Anime, Comment, Playlist, User

from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate


router_anime = APIRouter(
    prefix="/animes",
    tags=["animes"]
)

add_pagination(router_anime)

@router_anime.get("/get_all_anime", response_model=Page[ReadAnime])
async def get_anime(session: AsyncSession = Depends(get_async_session)):
    return await paginate(
        session, select(Anime)
    )




'''@router_anime.get("/get_all_anime")
async def get_anime(session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(
        select(Anime)
        .options(selectinload(Anime.playlist).subqueryload(Playlist.series))
        .options(selectinload(Anime.comment).selectinload(Comment.user).load_only(User.username))
    )
    return result.scalars().all()'''



@router_anime.get("/get_anime/{anime_id}")
async def get_anime(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(
        select(Anime)
        .filter(Anime.id == anime_id)
        .options(selectinload(Anime.playlist).subqueryload(Playlist.series))
        #.options(selectinload(Anime.comment).selectinload(Comment.user).load_only(User.username))
    )

    if result is None:
        raise HTTPException(status_code=404, detail="Anime not found")
    anime = result.scalar()
    return anime



@router_anime.post('/add_anime', response_model=None)
async def add_anime(new_anime: CreateAnime, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Anime).values(**new_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}


@router_anime.put('/update_anime', response_model=None)
async def add_anime(new_anime: CreateAnime, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Anime).values(**new_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}


@router_anime.delete('/delete_anime/{anime_id}', response_model=None)
async def add_anime(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Anime).where(Anime.id == anime_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}