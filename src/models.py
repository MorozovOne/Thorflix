from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, Boolean

metadata = MetaData()

rating = Table(
    "rating",
    metadata,
    Column("anime_id", Integer, ForeignKey("anime.id"), nullable=False),
    Column("user_id", Integer, ForeignKey("user.id"), nullable=False),
)