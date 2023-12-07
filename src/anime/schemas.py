from src.anime.models import AnimeCreate
from pydantic import BaseModel

class NewAnimeCreate(AnimeCreate):
    id: int
    name: str
    poster: str
    genre_name: str
    type: str
    episodes: int
    duration: str