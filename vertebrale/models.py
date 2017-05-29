from sqlalchemy import Column, Integer, String, Float

from base import Base

class Translation(Base)

class Food(Base):
    __tablename__ = 'ingredient'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    energy = Column(Float)
