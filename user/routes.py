from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from user.schema import UserCreate, UserBase, UserUpdate
from db import get_db
from user.repository import UserRepository
from user.services import UserService
from typing import List

user_router = APIRouter(prefix="/v1/users", tags=['users'])

user_repository = UserRepository()
user_service = UserService(user_repository=user_repository)

@user_router.post("/", response_model=UserCreate)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    
    return user_service.create_user(user_create, db)

@user_router.get("/", response_model=List[UserBase])
def get_all_users(db: Session = Depends(get_db)):
    
    return user_service.get_all_users(db)

@user_router.get("/{user_id}", response_model=UserBase)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user(db=db, user_id=user_id)
    
    if not user:
        return HTTPException(status_code=404, detail="user not found")
    
    return user

@user_router.put("/{user_id}", response_model=UserBase)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = user_service.update_user(user_id=user_id, username=user.username, db=db)
    
    if not updated_user:
        return HTTPException(status_code=404, detail="user not found")
    
    return updated_user

@user_router.delete("/delete/{user_id}", response_model=UserBase)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_service.delete_user(db=db, user_id=user_id)
    
    if not delete_user:
        return HTTPException(status_code=404, detail="user not found")
    
    return deleted_user