from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, func, Text
from sqlalchemy.orm import relationship
from db import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    reviews = relationship("Review", back_populates="user")