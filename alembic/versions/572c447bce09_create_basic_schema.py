"""create basic schema

Revision ID: 572c447bce09
Revises: 
Create Date: 2017-06-03 19:00:46.134324

"""
from alembic import op
from sqlalchemy import Integer, ForeignKey, String, Column, Float


# revision identifiers, used by Alembic.
revision = '572c447bce09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # create categories
    category = op.create_table(
        'category',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('parent_category', Integer, ForeignKey("category.id"), nullable=True)
    )

    parent = op.get_bind().execute(category.insert().values(name='Alkoholfreie Getränke')).inserted_primary_key[0]
    op.bulk_insert(category,
            [
                {'name': 'Kaffee', 'parent_category': parent},
                {'name': 'Sirup', 'parent_category': parent}
            ]
    )

    # create foods
    food = op.create_table(
        'food',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('energy', Float)
    )

    op.bulk_insert(food,
            [
                {'name': 'A', 'energy': 100.0},
                {'name': 'B', 'energy': 20.0},
                {'name': 'C', 'energy': 50.0}
            ]
    )


def downgrade():
    op.drop_table('category')
    op.drop_table('food')
