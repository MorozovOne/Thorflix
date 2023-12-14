from fastapi import APIRouter, Depends, Path, HTTPException
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload

from animes.schemas import CreateAnime, ReadAnime
from database import get_async_session
from models import Anime, Playlist



router_anime = APIRouter(
    prefix="/animes",
    tags=["animes"]
)



@router_anime.get("/get_all_anime")
async def get_anime(pagination_params: ReadAnime = Depends(), session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Anime)

        offset = (pagination_params.page - 1) * pagination_params.per_page
        query = query.offset(offset).limit(pagination_params.per_page)
        # --- Все что выше это фича пагинации
        result = await session.execute(query)
        anime = result.scalars().all()
        return anime

    except ValueError:
        raise HTTPException(status_code=422, detail="Value error")
    except BaseException:
        raise HTTPException(status_code=404, detail="Not found")




@router_anime.get("/get_anime/{anime_id}")
async def get_anime(anime_id: Annotated[int, Path(gt=0, lt=2147483647)], session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(
        select(Anime)
        .filter(Anime.id == anime_id)
        .options(selectinload(Anime.playlist).subqueryload(Playlist.series))
    )
    anime = result.scalar()
    return anime




@router_anime.post('/add_anime', response_model=None)
async def add_anime(new_anime: CreateAnime, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Anime).values(**new_anime.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "HTTP_200_OK"}
    except BaseException:
        raise HTTPException(status_code=400, detail="Bad Request")



@router_anime.put('/update_anime', response_model=None)
async def update_anime(id: int, payload: CreateAnime, session: AsyncSession = Depends(get_async_session)):
    query = (
        update(Anime)
        .where(id == Anime.id)
        .values(**payload.dict())
    )
    return await session.execute(query)

    '''stmt = update(Anime).values(**new_anime.dict())
    await session.execute(stmt)
    await session.commit()'''

    return {"status": "HTTP_200_OK"}




@router_anime.delete('/delete_anime/{anime_id}', response_model=None)
async def add_anime(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Anime).where(Anime.id == anime_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}