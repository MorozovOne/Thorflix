from fastapi import APIRouter
from fastapi_users import FastAPIUsers

from models import User
from .auth import auth_backend

from .schemas import UserRead, UserCreate

from .manager import get_user_manager


router_user = APIRouter()

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

router_user.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/jwt",
    tags=["auth"],
)

router_user.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/reg",
    tags=["auth"],
)