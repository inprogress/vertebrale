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

    def test_categories(self):
        from vertebrale.models import Category

        sub_category = Category(name='Sub')
        category = Category(name='Test')
        category.sub_categories.append(sub_category)
        db_session.add(category)
        db_session.commit()

        result = db_session.query(Category).all()
        self.assertEqual(len(result), 2)

        result = db_session.query(Category).filter(Category.parent_category == None).all()
        self.assertEqual(len(result), 1)
        self.assertEqual(len(result[0].sub_categories), 1)
