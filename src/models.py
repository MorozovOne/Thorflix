import datetime
import enum
from typing import Annotated

from pydantic import BaseModel
from sqlalchemy import (
    TIMESTAMP,
    CheckConstraint,
    Column,
    Enum,
    ForeignKey,
    Index,
    Integer,
    MetaData,
    PrimaryKeyConstraint,
    String,
    Table,
    text,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship, MappedColumn

from database import Base, str_256



metadata = MetaData()


'''user = Table(
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
'''


class Type(enum.Enum):
    TV = "TV"

class Genre(enum.Enum):
    Comedia = "Comedia"


class Anime(Base):
    __tablename__ = "anime"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    name: Mapped[str]
    poster: Mapped[str]
    type: Mapped[Type | None]
    genre: Mapped[Genre | None]
    episodes: Mapped[int]
    duration: Mapped[str]
    comment = relationship("Comment", back_populates="anime")


class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("anime.id", ondelete="CASCADE"))
    text: Mapped[str]
    anime = relationship("Anime", back_populates="comment")