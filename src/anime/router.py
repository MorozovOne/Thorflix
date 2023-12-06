from fastapi import FastAPI, APIRouter

router_anime = APIRouter(
    prefix="/anime",
    tags=["anime"]
)

@router_anime.get("/{anime_id}")
async def get():
    return "{ anime_id: 1; }"