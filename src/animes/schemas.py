from pydantic import BaseModel, Field, field_validator, ValidationInfo, validator
from typing import Optional

from typing_extensions import Annotated

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
    page: int = Field(gt=0, lt=10)
    per_page: int



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