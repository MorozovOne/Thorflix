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

class Comment(Base):
    __tablename__ = "comment"

    id: Mapped[int] = MappedColumn("id", Integer, primary_key=True)
    anime_id: Mapped[int] = mapped_column(ForeignKey("anime.id", ondelete="CASCADE"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id", ondelete="CASCADE"))
    text: Mapped[str]
    anime = relationship("Anime", back_populates="comment")
    user = relationship("User", back_populates="comment")