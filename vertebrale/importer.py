import csv

from vertebrale.database import db_session
from vertebrale.models import Category 

def startImport():
    with open('data/GenericFoods.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        row = rows[0]
        row2index = dict()
        for i, e in enumerate(row):
            row2index[e] = i

        d = row2index["category D"]

        data = list(map(lambda x: x[d], rows[1:]))

        result = {}

        for i in data:
            if len(i) == 0:
                continue
            if i[0] not in result:
                result[i[0]] = i

        for key, category in result.items():
            c = Category(name=category)
            db_session.add(c)
        db_session.commit()
        print("Import categories done!")
