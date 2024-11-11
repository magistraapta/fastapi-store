from sqlalchemy.orm import Session
from db import Base
from product.model import Product
from datetime import datetime

class ProductRepository:
    
    def create_product(self, product: Product, db: Session):
        db.add(product)
        db.commit()
        db.refresh(product)
        
        return product
    
    def get_all_products(self, db: Session):
        return db.query(Product).all()
    
    def get_product(self, product_id: int, db: Session):
        return db.query(Product).filter(Product.id == product_id).first()
    
    def delete(self, product_id: int, db: Session):
        product = db.query(Product).filter(Product.id == product_id).first()
        
        if product:
            self.db.delete(product)
            self.db.commit()
            
        return product