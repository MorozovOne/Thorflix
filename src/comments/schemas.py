from pydantic import BaseModel
from typing import Optional, List

from auth.schemas import UserRead, UserComment
from models import User


class AddComment(BaseModel):
    id: int
    anime_id: int
    user_id: int
    text: str

    class Config:
        from_attributes = True


class ReadComment(BaseModel):
    id: int
    anime_id: int
    user_id: int
    text: str
    user: List[UserComment]

    class Config:
        from_attributes = True