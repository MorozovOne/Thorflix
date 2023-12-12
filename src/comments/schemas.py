from pydantic import BaseModel
from typing import Optional

class AddComment(BaseModel):
    id: int
    anime_id: int
    user_id: int
    text: str

    class Config:
        from_attributes = True