from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from product.schema import ProductResponse, ProductCreate, ProductListResposne
from db import get_db
from product.repository import ProductRepository
from product.services import ProductServices
from typing import List

product_router = APIRouter(prefix="/v1/products", tags=["products"])

product_repository = ProductRepository()
product_service = ProductServices(product_repository=product_repository)

@product_router.get("/", response_model=ProductListResposne)
def get_all_products(db: Session = Depends(get_db)):
    try:
        products = product_service.get_all_products(db)
        
        return {
            "message": "Success retrieved all products",
            "products": products
        }
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
            "message": f"Internal server error: {e}"
        })
        
@product_router.get("/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    try:
        product = product_service.get_products(db=db, product_id=product_id)
        
        if not product:
            return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={
                "message": "Item not found",
            })
        return {
            "message": "Success retrieved product",
            "product": product
        }
    except Exception as e:
        return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content={
            "message": f"Internal Server Error: {e}"
        })

@product_router.post("/", response_model=ProductResponse)
def create_product(product_create: ProductCreate, db: Session = Depends(get_db)):
    try:
        
        return product_service.create_product(db=db, product=product_create)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating product: {e}")