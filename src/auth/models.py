from sqlalchemy import MetaData, Integer, String, Column, Boolean, Table
from sqlalchemy.orm import relationship

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


'''class User(SQLAlchemyBaseUserTable[int], base):
    id: int = Column(Integer, primary_key=True),
    username: str = Column(String, nullable=False),
    email: str = Column(String, nullable=False),
    status: str = Column(String, nullable=True),
    hashed_password: str = Column(String, nullable=False),
    is_active: bool = Column(Boolean, nullable=False, default=False),
    is_superuser: bool = Column(Boolean, nullable=False, default=False),
    is_verified: bool = Column(Boolean, nullable=False, default=False),'''