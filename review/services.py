from review.repository import ReviewRepository
from review.schema import ReviewResponse, ReviewBase, ReviewCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from review.model import Review
from user.model import User
from datetime import datetime

class ReviewService: 
    def __init__(self, review_repository: ReviewRepository) -> None:
        self.review_repository = review_repository

    def get_all_reviews(self, db: Session):
        reviews = self.review_repository.get_all_reviews(db=db)
        return [ReviewResponse(**review) for review in reviews]

    
    def create_review(self, db: Session, review: ReviewCreate, user_id: int, product_id: id):
        review = Review(
            content = review.content,
            user_id = user_id,
            product_id = product_id
        )
        
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            review.username = user.username
        
        return self.review_repository.create_review(db=db, review=review)