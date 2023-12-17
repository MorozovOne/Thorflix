from pydantic import BaseModel


class CreateComment(BaseModel):
    id: int
    anime_id: int
    user_id: int
    text: str

    class Config:
        from_attributes = True


class ReadComment(BaseModel):
    page: int = 1
    per_page: int = 2

    class Config:
        from_attributes = True


class UpdateComment(BaseModel):
    anime_id: int
    user_id: int
    text: str

    class Config:
        from_attributes = True