"""create basic schema

Revision ID: 572c447bce09
Revises: 
Create Date: 2017-06-03 19:00:46.134324

"""
from alembic import op
from sqlalchemy import Integer, ForeignKey, String, Column


# revision identifiers, used by Alembic.
revision = '572c447bce09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
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


def downgrade():
    op.drop_table('category')
