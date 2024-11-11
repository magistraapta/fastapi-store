from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ReviewBase(BaseModel):
    content: str

class ReviewCreate(ReviewBase):
    user_id: int
    product_id: int

class ReviewResponse(ReviewBase):
    id: int
    user_id: int
    product_id: int
    username: str

    class Config:
        orm_mode = True