import unittest
from sqlalchemy import create_engine
from vertebrale.database import db_session, init_db, Base

class TestDatabase(unittest.TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        db_session.configure(bind=engine)
        init_db(engine)

    def tearDown(self):
        db_session.remove()

    def test_init_empty_db(self):
        from vertebrale.models import Food
        result = db_session.query(Food).all()
        self.assertEqual(len(result), 0)
