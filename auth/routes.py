from fastapi import APIRouter, status, HTTPException, Depends
from user.schema import UserBase
import utils
from db import get_db
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from user.model import User
from user.schema import UserLogin
from auth.auth import create_access_token, get_current_user
from user.schema import Token


auth_router = APIRouter(prefix='/auth', tags=['auth'])

@auth_router.post("/login", response_model=Token)
def login(login_data: UserLogin, db: Session = Depends(get_db)):
    
    try:
        
        user = db.query(User).filter(User.username == login_data.username).first()
        
        if not user or not utils.verify_password(login_data.password, user.password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token = create_access_token(data={"sub": user.username})
        
        return {"access_token": access_token, "token_type": "bearer"}
    except HTTPException as e:
        return {"message": f"login failed: {e}"}


@auth_router.get("/users/me", response_model=UserBase)
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user