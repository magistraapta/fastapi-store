from sqlalchemy.orm import Session
from db import Base
from review.model import Review
from user.model import User


class ReviewRepository:
    
    def get_all_reviews(self, db: Session):
        # Join the Review and User tables to get the reviews with the associated username
        reviews = (
            db.query(Review, User.username)
            .join(User, Review.user_id == User.id)
            .all()
        )
        
        # Process the results to make sure they are returned in a usable format
        return [
            {
                "id": review.Review.id,
                "content": review.Review.content,
                "user_id": review.Review.user_id,
                "product_id": review.Review.product_id,
                "username": review.username
            }
            for review in reviews
        ]
    
    def create_review(self, db: Session, review: Review):
        db.add(review)
        db.commit()
        db.refresh(review)
        
        return review
    
    def get_user_by_username(self, db: Session, username: str, user: User):
        db.query(user).filter(user.username == username).first()
    