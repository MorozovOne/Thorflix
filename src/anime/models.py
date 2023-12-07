from sqlalchemy import MetaData, Integer, String, ForeignKey, Column
from sqlalchemy.orm import relationship
from pydantic import BaseModel

from src.database.base.core import Base

from src.comment.models import Comment

metadata = MetaData()


'''anime = Table(
    "anime",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("poster", String, nullable=False),
    Column("genre_id", Integer, ForeignKey("genre.id")),
    Column("type", String, nullable=False),
    Column("episodes", Integer, nullable=False),
    Column("duration", String, nullable=False),
)

genre = Table(
    "genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)'''



#SQL алхимия виувиу
class Anime(Base):
    __tablename__ = "anime"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    poster = Column(String, nullable=False)
    genre_name = Column(String, ForeignKey("genre.name"))
    type = Column(String, ForeignKey("type_anime.name"))
    episodes = Column(Integer, nullable=False)
    duration = Column(String, nullable=False)

    genre = relationship("Genre", back_populates="anime")
    type_anime = relationship("TypeAnime", back_populates="anime")
    comments = relationship(Comment, back_populates="anime")


# Модель самого пайдантика
class AnimeCreate(BaseModel):
    id: int
    name: str
    poster: str
    genre_name: str
    type: str
    episodes: int
    duration: str

class AnimeRead(BaseModel):
    id: int
    name: str
    poster: str
    genre_name: str
    type: str
    episodes: int
    duration: str

    class Config:
        from_attributes = True




class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    anime = relationship("Anime", back_populates="genre")


class GenreCreate(BaseModel):
    name: str


class GenreRead(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class TypeAnime(Base):
    __tablename__ = "typeanime"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    anime = relationship("Anime", back_populates="type_anime")
