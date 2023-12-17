import secrets

from fastapi import APIRouter, UploadFile, Depends, Path, HTTPException
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload

from animes.schemas import CreateAnime, ReadAnime, UpdateAnime
from core.database import get_async_session
from core.models import Anime, Playlist



router_anime = APIRouter(
    prefix="/animes",
    tags=["animes"]
)


'''@router_anime.post("/uploadfile")
async def create_upload_file(file: UploadFile = File(...), session: AsyncSession = Depends(get_async_session)):

    FILEPATH = 'files/'
    filename = file.filename

    extension = filename.split(".")[1]

    token_name = secrets.token_hex(10) +"."+extension
    generated_name = FILEPATH + token_name
    file_content = await file.read()

    with open(generated_name, "wb") as file:
        file.write(file_content)

    file.close()

    file_url = Path("localhost:8000/" + generated_name)
    return { "HTTP_200_OK" }
'''


@router_anime.get("/get_all_anime")
async def get_anime(pagination_params: ReadAnime = Depends(), session: AsyncSession = Depends(get_async_session)):
    try:
        query = select(Anime)

        offset = (pagination_params.page - 1) * pagination_params.per_page
        query = query.offset(offset).limit(pagination_params.per_page).order_by(Anime.id)
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
    anime = result.scalars().all()
    return anime



@router_anime.post('/add_poster')
async def add_poster(
        poster: UploadFile,
        logo: UploadFile,
        cover: UploadFile,
        anime_id: int,
        session: AsyncSession = Depends(get_async_session)
):
    poster_name = poster.filename
    logo_name = logo.filename
    cover_name = cover.filename

    split_poster = poster_name.split(".")[1]
    split_logo = logo_name.split(".")[1]
    split_cover = cover_name.split(".")[1]

    token_name_poster = secrets.token_hex(10) + "." + split_poster
    token_name_logo = secrets.token_hex(10) + "." + split_logo
    token_name_cover = secrets.token_hex(10) + "." + split_cover

    generated_name_poster = 'files/posters/' + token_name_poster
    generated_name_logo = 'files/logos/' + token_name_logo
    generated_name_cover = 'files/covers/' + token_name_cover

    content_poster = await poster.read()
    content_logo = await logo.read()
    content_cover = await cover.read()

    with open(generated_name_poster, "wb") as file:
        file.write(content_poster)
    with open(generated_name_logo, "wb") as file:
        file.write(content_logo)
    with open(generated_name_cover, "wb") as file:
        file.write(content_cover)
    file.close()


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



@router_anime.post(
    '/add_anime',
    response_model=None
)
async def add_anime(new_anime: CreateAnime, session: AsyncSession = Depends(get_async_session)):
    try:
        stmt = insert(Anime).values(**new_anime.dict())
        await session.execute(stmt)
        await session.commit()
        return {"status": "HTTP_200_OK"}

    except BaseException:
        raise HTTPException(status_code=400, detail="Bad Request")




@router_anime.put(
    '/update_anime',
    response_model=None
)
async def update_anime(id: int, update_anime: UpdateAnime, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Anime).where(Anime.id == id).values(**update_anime.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}




@router_anime.delete('/delete_anime/{anime_id}', response_model=None)
async def add_anime(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Anime).where(Anime.id == anime_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}