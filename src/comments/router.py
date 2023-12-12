from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from comments.schemas import AddComment
from database import get_async_session
from models import Comment, User

router_comment = APIRouter(
    prefix="/comments",
    tags=["comments"]
)




@router_comment.get('/get_comment/{comment_id}', response_model=None)
async def add_anime(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(
        select(Comment)
        .filter(Comment.id == comment_id)
        .options(selectinload(Comment.user).load_only(User.username))
    )
    comment = result.scalar()
    return comment


@router_comment.post('/add_comment', response_model=None)
async def add_anime(add_comment: AddComment, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Comment).values(**add_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}

@router_comment.put('/update_comment', response_model=None)
async def add_anime(add_comment: AddComment, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Comment).values(**add_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}

@router_comment.delete('/delete_comment/{comment_id}', response_model=None)
async def add_anime(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Comment).where(Comment.id == comment_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}