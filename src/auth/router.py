from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
from fastapi_users import FastAPIUsers

from auth.models import User
from config import REDIS_HOST
from .auth import auth_backend

from .schemas import UserRead, UserCreate
from .manager import get_user_manager

from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from core.database import get_async_session



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
@cache(expire=300)
async def get_user(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    query = await session.execute(select(User).filter(User.id == user_id))
    user = query.scalar()
    return user

@router_user.on_event("startup")
async def startup():
    redis = aioredis.from_url(f"redis://{REDIS_HOST}")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")