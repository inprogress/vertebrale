"""create basic schema

Revision ID: 572c447bce09
Revises: 
Create Date: 2017-06-03 19:00:46.134324

"""
from alembic import op
from sqlalchemy import Integer, ForeignKey, String, Column, Float
import csv

# revision identifiers, used by Alembic.
revision = '572c447bce09'
down_revision = None
branch_labels = None
depends_on = None

csvfile = open('alembic/versions/initial_data/GenericFoods.csv', 'r')
reader = csv.reader(csvfile)
rows = list(reader)

# the header of the csv, easy lookup
header = {}

for i, e in enumerate(rows[0]):
    header[e] = i

normalized_categories = {'name': 'root', 'children': []}

# categories are stored per item in hierarchy with / as seperator
all_categories = list(map(lambda row: row[header['category D']], rows[1:]))

for categories in all_categories:
    hierarchy = categories.split('/')
    current_node = normalized_categories['children']
    for category in hierarchy:
        if len(category) == 0:
            continue
        result = list(filter(lambda x: x['name'] == category, current_node))
        if len(result) == 0:
            next_node = {'name': category, 'children': []}
            current_node.append(next_node)
            current_node = next_node['children']
            continue
        current_node = result[0]['children']

def create_categories(parentId, children, table):
    print(len(children))
    for child in children:
        parent = None
        if parentId != None:
            parent = op.get_bind().execute(table.insert().values(name=child['name'], parent_category=parentId)).inserted_primary_key[0]
        else:
            parent = op.get_bind().execute(table.insert().values(name=child['name'])).inserted_primary_key[0]

        if len(child['children']) > 0:
            create_categories(parent, child['children'], table)

def upgrade():
    # create categories
    category = op.create_table(
        'category',
        Column('id', Integer, primary_key=True),
        Column('name', String, nullable=False),
        Column('parent_category', Integer, ForeignKey("category.id"), nullable=True)
    )

    root = normalized_categories['children']
    create_categories(None, root, category)

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
