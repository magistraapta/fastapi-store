from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime
from review.schema import ReviewBase

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: int
    stock: int
    image_url: Optional[str] = "/static/image/not-found.png"

class ProductResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: int
    stock: int
    image_url: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True