from sqlalchemy import Column, Integer, String, Float

from database import Base

class Ingredient(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    energy = Column(Float)
