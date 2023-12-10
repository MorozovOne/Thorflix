from pydantic import BaseModel
from typing import Optional

from models import Genre, Type


class AnimeSchema(BaseModel):
    id: int
    name: str
    poster: str
    type: Optional[Type]
    genre: Optional[Genre]
    episodes: int
    duration: str

    class Config:
        from_attributes = True

'''from src.models import AnimeCreate
from pydantic import BaseModel

class NewAnimeCreate(AnimeCreate):
    id: int
    name: str
    poster: str
    genre_name: str
    type: str
    episodes: int
    duration: str'''