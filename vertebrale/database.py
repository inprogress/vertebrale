from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from vertebrale.base import Base

# could be postgres
engine = create_engine('sqlite:///data/data.db')
db_session = scoped_session(sessionmaker(autocommit=False,autoflush= False, bind=engine))

Base.query = db_session.query_property()

def init_db(actualEngine=engine):
    import vertebrale.models
    Base.metadata.create_all(bind=actualEngine)
