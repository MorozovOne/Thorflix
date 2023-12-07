from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, Boolean
from sqlalchemy.orm import declarative_base, relationship
from pydantic import BaseModel

from src.database.base.core import Base


metadata = MetaData()


comment = Table(
    "comment",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("anime_id", Integer, ForeignKey("genre.id")),
    Column("user_id", String, ForeignKey("user.id")),
    Column("username", Integer, ForeignKey("user.username")),
    Column("text", String, nullable=False),
)

class Comment(Base):
    __tablename__ = "comments"
    id = Column(Integer, primary_key=True)
    anime_id = Column(Integer, ForeignKey("anime.id"))
    user_id = Column(Integer, ForeignKey("user.id"))
    username = Column(String, ForeignKey("user.username"))
    text = Column(String, nullable=False)
    anime = relationship("Anime", back_populates="comments")

class AnimeCreate(BaseModel):
    id: int
    anime_id: int
    user_id: int
    username: str
    text: str

class AnimeRead(BaseModel):
    id: int
    anime_id: int
    user_id: int
    username: str
    text: str

    class Config:
        from_attributes = True