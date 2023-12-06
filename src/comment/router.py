from fastapi import FastAPI, APIRouter

router_comment = APIRouter(
    prefix="/comment",
    tags=["comment"]
)

@router_comment.get("/{comment_id}")
async def get():
    return "{ comment_id: 1; }"