import enum

from sqlalchemy import (
    ForeignKey,
    Integer,
    MetaData,
    String,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn

from animes.genre import GenreAnime
from core.database import Base

metadata = MetaData()

class Status(enum.Enum):
    Ongoing = "Онгоинг"
    Exit = "Вышел"
    Announcement = "Анонс"


class TypeAnime(enum.Enum):
    TV = "ТВ Сериал"
    Film = "Фильм"
    OVA = "OVA"
    Special = "Спешл"


class Anime(Base):
    __tablename__ = "anime"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    name: Mapped[str]
    poster: Mapped[str]
    logo: Mapped[str]
    cover: Mapped[str]
    type: Mapped[TypeAnime | None]
    genre: Mapped[GenreAnime | None]
    season: Mapped[str]
    duration: Mapped[str]
    description: Mapped[str] = MappedColumn(String(255))
    status: Mapped[Status | None]
    age: Mapped[int]
    year: Mapped[int]

    comment = relationship("Comment", back_populates="anime")
    playlist = relationship("Playlist", back_populates="anime")


class Playlist(Base):
    __tablename__ = "playlist"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("anime.id", ondelete="CASCADE"))

    anime = relationship("Anime", back_populates="playlist")
    series = relationship("Series", back_populates="playlist")


class Series(Base):
    __tablename__ = "series"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    which: Mapped[int]
    name: Mapped[str]
    playlist_id: Mapped[int] = mapped_column(ForeignKey("playlist.id", ondelete="CASCADE"))
    time: Mapped[str]
    fhd: Mapped[str]
    hd: Mapped[str]
    sd: Mapped[str]
    release: Mapped[str]

    playlist = relationship("Playlist", back_populates="series")