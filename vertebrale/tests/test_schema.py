from snapshottest import TestCase
from sqlalchemy import create_engine
from vertebrale.database import db_session, init_db
from graphene.test import Client
from vertebrale.schema import schema

class TestSchema(TestCase):
    def test_food(self):
        engine = create_engine('sqlite:///:memory:')
        db_session.configure(bind=engine)
        init_db(engine)

        from vertebrale.models import Food
        db_session.add(Food(name='A', energy=1))
        db_session.add(Food(name='B', energy=1))
        db_session.commit()

        client = Client(schema)
        self.assertMatchSnapshot(client.execute('''{ foods { name } }'''))
