from sqlalchemy.orm import Session
from db import Base
from user.model import User
from typing import Optional

class UserRepository:
    
    def create_user(self, user: User, db: Session):
        db.add(user)
        db.commit()
        db.refresh(user)
        
        return user
    
    def get_all_users(self, db: Session):
        users = db.query(User).all()
        return users
    
    def get_user(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()
    
    def update_user(self, db: Session, user_id: int, username: str = None):
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            if username:
                user.username = username
                
                
        db.commit()
        db.refresh(user)
        return user
            
    
    def delete(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        
        if user:
            db.delete(user)
            db.commit()        
                
        return user
    
    def get_user_by_name(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(User.username == username).first()