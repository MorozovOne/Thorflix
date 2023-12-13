from fastapi import FastAPI
from fastapi_pagination import add_pagination

from animes.router import router_anime
from auth.router import router_user

'''from auth.router import router_user'''
from comments.router import router_comment



app = FastAPI(
    title='Thorflix',
    description='API is'
)


app.include_router(router_user, prefix="/auth", tags=["auth"])
app.include_router(router_anime)
app.include_router(router_comment)


add_pagination(app)