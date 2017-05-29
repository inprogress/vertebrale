from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine('sqlite:///:memory:')
db_session = scoped_session(sessionmaker(autocommit=False,autoflush= False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    print('Init DB')
    from models import Ingredient
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    i1 = Ingredient(name='Agar Agar', energy=641)
    i2 = Ingredient(name='Fotzelschnitte ungezuckert', energy=939)
    db_session.add(i1)
    db_session.add(i2)
    db_session.commit()
