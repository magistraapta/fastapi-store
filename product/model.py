from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, Text
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Integer, nullable=False)
    stock = Column(Integer, nullable=False)
    image_url = Column(Text, default="/static/image/not-found.png")
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), nullable=False)
    
    reviews = relationship("Review", back_populates="product")