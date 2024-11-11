from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    id: int
    username: str

class UserCreate(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True
        
class UserUpdate(BaseModel):
    username: Optional[str] = None  # `username` is optional
    password: Optional[str] = None 

    class Config:
        orm_mode = True
        
