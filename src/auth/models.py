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

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String, nullable=False),
    Column("status", String, nullable=True),
    Column("picture", String, nullable=True),
    Column("profile_cover", String, nullable=True),
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
    picture: Mapped[str] = mapped_column(
        nullable=True
    )
    profile_cover: Mapped[str] = mapped_column(
        nullable=True
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