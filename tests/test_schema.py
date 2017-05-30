from snapshottest import TestCase
from sqlalchemy import create_engine
from vertebrale.database import db_session, init_db
from graphene.test import Client
from vertebrale.schema import schema

class TestSchema(TestCase):
    def setUp(self):
        engine = create_engine('sqlite:///:memory:')
        db_session.configure(bind=engine)
        init_db(engine)
        from vertebrale.models import Food
        db_session.add(Food(name='A', energy=1))
        db_session.add(Food(name='B', energy=1))
        db_session.commit()
        self.client = Client(schema)

    def tearDown(self):
        db_session.remove()

    def test_food(self):
        self.assertMatchSnapshot(self.client.execute('''{ foods { name } }'''))

    def test_filter_food(self):
        query = ''' {
            foods(name: "A") {
                id
                name
                energy
            }
        }
        '''.strip()
        self.assertMatchSnapshot(self.client.execute(query))
