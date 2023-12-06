from fastapi import FastAPI, APIRouter

router_anime = APIRouter(
    prefix="/anime",
    tags=["Anime"]
)

@router_anime.get("/{anime_id}")
async def get():
    return "hello"