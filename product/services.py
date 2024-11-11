from product.repository import ProductRepository
from product.schema import ProductCreate
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from product.model import Product
from datetime import datetime

class ProductServices:
    
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
        
    def create_product(self, product: ProductCreate, db: Session):
        product = Product(
            name = product.name,
            description = product.description,
            price = product.price,
            stock = product.stock,
            image_url = product.image_url,
            created_at = datetime.now(),
            updated_at = datetime.now()
        )
        
        return self.product_repository.create_product(product=product, db=db)
    
    def get_all_products(self, db: Session):
        return self.product_repository.get_all_products(db=db)
    
    def get_products(self, db: Session, product_id: int):
        return self.product_repository.get_product(db=db, product_id=product_id)