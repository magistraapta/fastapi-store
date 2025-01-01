from fastapi import APIRouter, status, HTTPException, Depends
from user.schema import UserBase
from fastapi.responses import JSONResponse
import utils
from db import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from user.model import User
from user.schema import UserLogin
from auth.auth import create_access_token, get_current_user
from user.schema import Token
from pydantic import BaseModel

class LoginRequest(BaseModel):
    username: str
    password: str

auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post("/login", response_model=Token)
def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    
    try:
        
        user = db.query(User).filter(User.username == login_data.username).first()
        
        if not user or not utils.verify_password(login_data.password, user.password):
            return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
                "message": "Incorrect Username or Password"
            })
        access_token = create_access_token(data={"sub": user.username})
        
        return {"user": user, "access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={"message": f"{e}"})


@auth_router.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user