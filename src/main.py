from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache

from redis import asyncio as aioredis
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination
from fastapi.staticfiles import StaticFiles

from animes.router import router_anime
from auth.router import router_user

from comments.router import router_comment
from config import REDIS_HOST

app = FastAPI(
    title='Thorflix',
    description='API is'
)


app.mount("/files", StaticFiles(directory="files"), name='images')
app.include_router(router_user, prefix="/user", tags=["user"])
app.include_router(router_anime)
app.include_router(router_comment)


origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

add_pagination(app)
