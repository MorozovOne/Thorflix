from fastapi import FastAPI

from anime.router import router_anime
from auth.router import router_user

app = FastAPI()

app.include_router(router_user, prefix="/auth", tags=["auth"])

app.include_router(router_anime)