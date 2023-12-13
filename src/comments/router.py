from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy import insert, update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from comments.schemas import AddComment, ReadComment
from database import get_async_session
from models import Comment, User

from fastapi_pagination import Page, add_pagination
from fastapi_pagination.ext.sqlalchemy import paginate


router_comment = APIRouter(
    prefix="/comments",
    tags=["comments"]
)

add_pagination(router_comment)

@router_comment.get('/get_comment/{anime_id}', response_model=Page[ReadComment])
async def get_comment(anime_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await paginate(
        session, select(Comment)
        .filter(Comment.anime_id == anime_id)
        .options(selectinload(Comment.user).load_only(User.username))
    )
    print(User.model_dump())





'''@router_comment.get('/get_comment/{comment_id}', response_model=None)
async def add_anime(comment_id: int, session: AsyncSession = Depends(get_async_session)):
    result = await session.execute(
        select(Comment)
        .filter(Comment.id == comment_id)
        .options(selectinload(Comment.user).load_only(User.username))
    )
    comment = result.scalar()
    return comment'''


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