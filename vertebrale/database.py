from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from base import Base

# could be postgres
engine = create_engine('sqlite:///:memory:')
db_session = scoped_session(sessionmaker(autocommit=False,autoflush= False, bind=engine))

Base.query = db_session.query_property()

def init_db(actualEngine=engine):
    from models import Food
    Base.metadata.create_all(bind=actualEngine)
