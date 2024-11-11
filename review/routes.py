from fastapi import APIRouter, Depends, HTTPException, Request
from sqlalchemy.orm import Session
from review.schema import ReviewBase, ReviewCreate, ReviewResponse
from db import get_db
from review.repository import ReviewRepository
from review.services import ReviewService
from typing import List

review_router = APIRouter(prefix="/v1/reviews", tags=["reviews"])

review_repository = ReviewRepository()
review_service = ReviewService(review_repository=review_repository)

@review_router.get("/", response_model=List[ReviewResponse])
def get_all_reviews(db: Session = Depends(get_db)):
    return review_service.get_all_reviews(db=db)

@review_router.post("/", response_model=ReviewResponse)
def create_review(review_create: ReviewBase, user_id: int, product_id: int, db: Session = Depends(get_db)):
    return review_service.create_review(db=db, review=review_create, user_id=user_id, product_id=product_id)