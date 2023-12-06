'''from sqlalchemy import MetaData, Integer, String, ForeignKey, Table, Column, Boolean

metadata = MetaData()

anime = Table(
    "anime",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("poster", String, nullable=False),
    Column("genre_id", Integer, ForeignKey("genre.id")),
    Column("type", String, nullable=False),
    Column("episodes", Integer, nullable=False),
    Column("duration", String, nullable=False),
)

genre = Table(
    "genre",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
)'''