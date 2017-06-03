from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum 
from sqlalchemy.orm import relationship
import enum

from vertebrale.base import Base

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    sub_categories = relationship('Category')
    parent_category = Column(Integer, ForeignKey('category.id'))

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    energy = Column(Float)
