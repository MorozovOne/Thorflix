from fastapi import APIRouter, UploadFile, Depends, Path, HTTPException
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from pydantic import ValidationError
from redis import asyncio as aioredis
from typing_extensions import Annotated

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload

from animes.models import Anime, Playlist, Series
from animes.schemas import CreateAnime, ReadAnime, UpdateAnime
from animes.utils import upload_logo, upload_cover, upload_poster
from core.config import get_settings
from core.database import get_async_session


router_anime = APIRouter(
    prefix="/animes",
    tags=["animes"]
)


@router_anime.get("/get_series/{series_id}")
async def get_series(
        series_id: Annotated[int, Path(gt=0, lt=2147483647)],
        session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Series).where(Series.id == series_id))
    anime = result.scalars().all()
    if not anime:
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return {"anime": anime}



@router_anime.get("/get_all_anime")
@cache(expire=180)
async def get_anime(
        pagination_params: ReadAnime = Depends(),
        session: AsyncSession = Depends(get_async_session)
):
    query = select(Anime)
    # --- Пагинация
    offset = (pagination_params.page - 1) * pagination_params.per_page
    query = query.offset(offset).limit(pagination_params.per_page).order_by(Anime.id)
    # --- Пагинация
    result = await session.execute(query)
    anime = result.scalars().all()
    return anime





@router_anime.get("/get_anime/{anime_id}")
@cache(expire=180)
async def get_anime(
        anime_id: Annotated[int, Path(gt=0, lt=2147483647)],
        session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(
        select(Anime)
        .filter(Anime.id == anime_id)
        .options(selectinload(Anime.playlist).subqueryload(Playlist.series))
    )
    anime = result.scalars().all()
    return anime



@router_anime.post('/add_poster')
async def add_poster(
        anime_id: int,
        poster: UploadFile = None,
        logo: UploadFile = None,
        cover: UploadFile = None,
        session: AsyncSession = Depends(get_async_session)
):
    try:
        if poster:
            generated_name_poster = await upload_poster(poster)
        else:
            generated_name_poster = "None"

        if logo:
            generated_name_logo = await upload_logo(logo)
        else:
            generated_name_logo = "None"

        if cover:
            generated_name_cover = await upload_cover(cover)
        else:
            generated_name_cover = "None"

    except:
        raise HTTPException(status_code=405, detail="sorry its not upload")

    stmt = (
        update(Anime).
        where(Anime.id == anime_id).
        values(
            poster=generated_name_poster,
            logo=generated_name_logo,
            cover=generated_name_cover
        )
    )
    await session.execute(stmt)
    await session.commit()
    return {"result": "HTTP_200_OK"}



@router_anime.post('/add_anime', response_model=None)
async def add_anime(
        new_anime: CreateAnime,
        session: AsyncSession = Depends(get_async_session)
):

    try:
        stmt = insert(Anime).values(**new_anime.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "HTTP_200_OK"}

    except BaseException:
        raise HTTPException(status_code=400, detail="Bad Request")




@router_anime.put('/update_anime', response_model=None)
async def update_anime(
        id: int, update_anime: UpdateAnime,
        session: AsyncSession = Depends(get_async_session)
):
    stmt = update(Anime).where(Anime.id == id).values(**update_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}



@router_anime.delete('/delete_anime/{anime_id}', response_model=None)
async def add_anime(
        anime_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    stmt = delete(Anime).where(Anime.id == anime_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}



@router_anime.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{get_settings().get('redis_host')}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")