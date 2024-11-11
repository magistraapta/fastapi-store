from user.repository import UserRepository
from user.model import User
from user.schema import UserCreate, UserBase
from sqlalchemy.orm import Session
# from utils import get_hashed_password

class UserService:
    
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    
    def create_user(self, user_create: UserCreate, db: Session):
        user = User(
            username = user_create.username,
            # password = get_hashed_password(password=user_create.password)
            password = user_create.password
        )
        
        return self.user_repository.create_user(user=user, db=db)
        
    def get_all_users(self, db: Session):
        return self.user_repository.get_all_users(db=db)
    
    def get_user(self, db: Session, user_id: int) -> User:
        return self.user_repository.get_user(db, user_id)
    
    def update_user(self, db: Session, user_id: int, username: str = None):
        return self.user_repository.update_user(db=db, user_id=user_id, username=username)
    
    def delete_user(self, db: Session, user_id: int):
        return self.user_repository.delete(db=db, user_id=user_id)