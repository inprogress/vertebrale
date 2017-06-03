from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from migrate import *

meta = MetaData()

category = Table(
    'category',
    meta,
    Column('id', Integer, primary_key=True),
    Column('name', String, nullable=False),
    Column('parent_category', Integer, ForeignKey("category.id"), nullable=True),
)

def upgrade(migrate_engine):
    meta.bind = migrate_engine
    category.create()

def downgrade(migrate_engine):
    meta.bind = migrate_engine
    category.drop()
