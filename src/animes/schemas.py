from pydantic import BaseModel
from typing import Optional

from models import GenreAnime, TypeAnime


class CreateAnime(BaseModel):
    id: int
    name: str
    poster: str
    type: Optional[TypeAnime]
    genre: Optional[GenreAnime]
    episodes: int
    duration: str

    class Config:
        from_attributes = True


class ReadAnime(BaseModel):
    id: int
    name: str
    poster: str
    type: Optional[TypeAnime]
    genre: Optional[GenreAnime]
    episodes: int
    duration: str

    class Config:
        from_attributes = True