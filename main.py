from fastapi import FastAPI

from src.anime.router import router_anime
from src.auth.router import router_user
from src.comment.router import router_comment

from src.anime.models import Anime

app = FastAPI()


app.include_router(router_user, prefix="/auth", tags=["auth"])
app.include_router(router_anime)
app.include_router(router_comment)