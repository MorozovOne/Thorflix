import uuid
from typing import Optional

from fastapi_users import schemas
from pydantic import EmailStr


class UserRead(schemas.BaseUser[int]):
    id: int
    username: str
    status: str
    picture: Optional[str] = None
    profile_cover: Optional[str] = None
    email: EmailStr
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserCreate(schemas.BaseUserCreate):
    id: int
    username: str
    status: str
    picture: Optional[str] = None
    profile_cover: Optional[str] = None
    email: EmailStr
    password: str
    is_active: Optional[bool] = True
    is_superuser: Optional[bool] = False
    is_verified: Optional[bool] = False


class UserUpdate(schemas.BaseUserUpdate):
    status: Optional[str] = None
    password: Optional[str] = None
    picture: Optional[str] = None
    profile_cover: Optional[str] = None
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    is_superuser: Optional[bool] = None
    is_verified: Optional[bool] = None


class UserComment(schemas.BaseUser[int]):
    id: int
    username: str

    class Config:
        from_attributes = True