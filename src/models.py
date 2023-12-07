from sqlalchemy import MetaData

from src.anime.models import Anime
from src.auth.models import user
from src.comment.models import Comment


metadata = MetaData()

__all__ = ("Anime", "user", "Comment")
