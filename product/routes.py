from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from product.schema import ProductResponse, ProductCreate
from db import get_db
from product.repository import ProductRepository
from product.services import ProductServices
from typing import List

product_router = APIRouter(prefix="/v1/products", tags=["products"])

product_repository = ProductRepository()
product_service = ProductServices(product_repository=product_repository)

@product_router.get("/", response_model=List[ProductResponse])
def get_all_products(db: Session = Depends(get_db)):
    try:
        
        return product_service.get_all_products(db=db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting all products: {e}")

@product_router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    try:
        
        return product_service.get_products(db=db, product_id=product_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error getting product: {e}")

@product_router.post("/", response_model=ProductResponse)
def create_user(product_create: ProductCreate, db: Session = Depends(get_db)):
    try:
        
        return product_service.create_product(db=db, product=product_create)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {e}")