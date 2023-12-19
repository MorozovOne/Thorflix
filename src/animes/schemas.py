from pydantic import BaseModel
from typing import Optional

from animes.models import GenreAnime, TypeAnime, Status


class CreateAnime(BaseModel):
    id: int
    name: str
    poster: str
    logo: str
    cover: str
    type: Optional[TypeAnime]
    genre: Optional[GenreAnime]
    season: str
    duration: str
    description: str
    status: Optional[Status]
    age: int
    year: int


    class Config:
        from_attributes = True


class ReadAnime(BaseModel):
    page: int = 1
    per_page: int = 2


    class Config:
        from_attributes = True


class UpdateAnime(BaseModel):
    name: str
    poster: str
    logo: str
    cover: str
    type: Optional[TypeAnime]
    genre: Optional[GenreAnime]
    season: str
    duration: str
    description: str
    status: Optional[Status]
    age: int
    year: int

    class Config:
        from_attributes = True

class UploadPoster(BaseModel):
    poster: str