from fastapi import APIRouter, Depends
from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from comments.schemas import CreateComment, ReadComment, UpdateComment
from core.database import get_async_session
from comments.models import Comment
from auth.models import User




router_comment = APIRouter(
    prefix="/comments",
    tags=["comments"]
)




@router_comment.get('/get_comments/')
async def get_comments(pagination_params: ReadComment = Depends(), session: AsyncSession = Depends(get_async_session)):
    query = select(Comment).options(selectinload(Comment.user).load_only(User.username))

    offset = (pagination_params.page - 1) * pagination_params.per_page
    query = query.offset(offset).limit(pagination_params.per_page).order_by(Comment.id)

    result = await session.execute(query)
    comments = result.scalars().all()

    return comments




@router_comment.post('/add_comment', response_model=None)
async def add_comment(add_comment: CreateComment, session: AsyncSession = Depends(get_async_session)):
    stmt = insert(Comment).values(**add_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}




@router_comment.put('/update_comment', response_model=None)
async def update_comment(id: int, update_comment: UpdateComment, session: AsyncSession = Depends(get_async_session)):
    stmt = update(Comment).where(Comment.id == id).values(**update_comment.dict())
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}




@router_comment.delete('/delete_comment/{comment_id}', response_model=None)
async def delete_comment(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    stmt = delete(Comment).where(Comment.id == comment_id)
    await session.execute(stmt)
    await session.commit()
    return {"status": "HTTP_200_OK"}