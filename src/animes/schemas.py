from fastapi import Path
from pydantic import BaseModel, ValidationError, model_validator
from typing import Optional, Annotated

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
    page: int = 1
    per_page: int = 2


    class Config:
        from_attributes = True