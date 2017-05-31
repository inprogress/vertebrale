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
        from vertebrale.models import Category, CategoryTranslation, LanguageCode

        cat_hello = Category()
        translation = CategoryTranslation(
                languageCode=LanguageCode.GERMAN,
                name='Hallo')
        cat_hello.translations.append(translation)

        db_session.add(cat_hello)
        db_session.add(translation)
        db_session.commit()
        db_session.query(CategoryTranslation)

        db_session.query()
        result = db_session.query(Category).all()
        self.assertEqual(len(result), 1)

        self.assertEqual(len(result[0].translations), 1)
