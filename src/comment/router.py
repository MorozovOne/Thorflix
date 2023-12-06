from fastapi import FastAPI, APIRouter

router_comment = APIRouter(
    prefix="/anime",
    tags=["Anime"]
)

@router_comment.get("/{comment_id}")
async def get():
    return "{" \
           "comment_id: 1" \
           "}"