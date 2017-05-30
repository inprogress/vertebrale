import unittest
from sqlalchemy import create_engine
from vertebrale.database import db_session, init_db, Base

class TestDatabase(unittest.TestCase):
    def test_init_empty_db(self):
        engine = create_engine('sqlite:///:memory:')
        db_session.configure(bind=engine)
        init_db(engine)
        
        from vertebrale.models import Food
        result = db_session.query(Food).all()
        self.assertEqual(len(result), 0)
