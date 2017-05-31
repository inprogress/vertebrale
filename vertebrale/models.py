from sqlalchemy import Column, Integer, String, Float, ForeignKey, Enum 
from sqlalchemy.orm import relationship
import enum

from vertebrale.base import Base

class LanguageCode(enum.Enum):
    GERMAN = 'de'
    FRENCH = 'fr'
    ITALIAN = 'it'
    ENGLISH = 'en'

class CategoryTranslation(Base):
    __tablename__ = 'translation'

    id = Column(Integer, primary_key=True)
    languageCode = Column(Enum(LanguageCode))
    name = Column(String)
    category = Column(Integer, ForeignKey('category.id'))

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    translations = relationship('CategoryTranslation')

class Food(Base):
    __tablename__ = 'food'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    energy = Column(Float)
