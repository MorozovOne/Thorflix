from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from comments.schemas import AddComment
from database import get_async_session
from models import Comment

router_comment = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

@router_comment.post('/add_comment', response_model=None)
async def add_anime(add_comment: AddComment, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Comment).values(**add_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}