from fastapi import APIRouter, Depends, HTTPException, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from user.schema import UserCreate, UserBase, UserUpdate, UserResponse, Token
from db import get_db
from user.repository import UserRepository
from user.services import UserService
from typing import List
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from user.model import User
import auth
from auth import get_current_user
import utils


user_router = APIRouter(prefix="/v1/users", tags=['users'])

user_repository = UserRepository()
user_service = UserService(user_repository=user_repository)

@user_router.post("/", response_model=UserResponse)
def create_user(user_create: UserCreate, db: Session = Depends(get_db)):
    try:
        user = user_service.create_user(user_create, db)
        
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content={
                "message": "User created successfully",
                "status": "success",
                "data": {
                    "id": user.id,
                    "username": user.username
                }
            }
        )
    except ValueError as e:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={
                "message": str(e),
                "status": "error",
                "data": None
            }
        )
    except Exception as e:
        # Handle other errors
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "message": "Internal server error",
                "status": "error",
                "data": None
            }
        )

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

@user_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.username == form_data.username).first()
    
    if not user or not utils.verify_password(form_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@user_router.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user