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



Base = declarative_base()

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("status", String, nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, nullable=False, default=False),
    Column("is_superuser", Boolean, nullable=False, default=False),
    Column("is_verified", Boolean, nullable=False, default=False),
)

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
    )
    username: Mapped[str] = mapped_column(
        String(length=200), nullable=False
    )
    status: Mapped[str] = mapped_column(
        String(length=200), nullable=True
    )
    email: Mapped[str] = mapped_column(
        String(length=320), unique=True, index=True, nullable=False
    )
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )

    comment = relationship("Comment", back_populates="user")


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

class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("anime.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    text: Mapped[str]
    anime = relationship("Anime", back_populates="comment")
    user = relationship("User", back_populates="comment")


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