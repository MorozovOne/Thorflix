import enum

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    Boolean,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn, declarative_base

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

class GenreAnime(enum.Enum):
    Genre1 = "Комедия"
    Genre2 = "Безумие"
    Genre3 = "Боевые искусства"
    Genre4 = "Вампиры"
    Genre5 = "Военное"
    Genre6 = "Гарем"
    Genre7 = "Демоны"
    Genre8 = "Дзёсэй"
    Genre9 = "Драма"
    Genre10 = "Исторический"
    Genre11 = "Космос"
    Genre12 = "Магия"
    Genre13 = "Машины"
    Genre14 = "Меха"
    Genre15 = "Музыка"
    Genre16 = "Повседневность"
    Genre17 = "Приключения"
    Genre18 = "Романтика"
    Genre19 = "Самураи"
    Genre20 = "Сверхъестественное"
    Genre21 = "Сёдзё"
    Genre22 = "Сёнэн"
    Genre23 = "Сёнэн - Aй"
    Genre24 = "Сэйнэн"
    Genre25 = "Триллер"
    Genre26 = "Ужасы"
    Genre27 = "Фантастика"
    Genre28 = "Фэнтези"
    Genre29 = "Школа"
    Genre30 = "Экшен"
    Genre31 = 'Этти'


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