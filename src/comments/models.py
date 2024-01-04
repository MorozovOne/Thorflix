from sqlalchemy import (
    MetaData, ForeignKey, Integer,
)
from sqlalchemy.orm import MappedColumn, Mapped, mapped_column, relationship

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