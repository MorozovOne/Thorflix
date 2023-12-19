from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from auth.models import User
from .auth import auth_backend

from .schemas import UserRead, UserCreate

from .manager import get_user_manager

from fastapi import APIRouter, UploadFile, Depends, Path, HTTPException, File
from typing_extensions import Annotated
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, insert, update, delete
from sqlalchemy.orm import selectinload

from animes.schemas import CreateAnime, ReadAnime, UpdateAnime
from core.database import get_async_session
from animes.models import Anime, Playlist



router_user = APIRouter()


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


router_user.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["user"],
)

router_user.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["user"],
)

router_user.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["user"],
)

router_user.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/reg",
    tags=["user"],
)

@router_user.get('/{user_id}',)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(User).filter(User.id == user_id))
    user = query.scalar()
    return user