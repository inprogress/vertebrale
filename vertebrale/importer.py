import csv

from vertebrale.database import db_session
from vertebrale.models import Category, CategoryTranslation, LanguageCode

def startImport():
    with open('data/GenericFoods.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        row = rows[0]
        row2index = dict()
        for i, e in enumerate(row):
            row2index[e] = i

        d = row2index["category D"]
        f = row2index["category F"]
        i = row2index["category I"]
        e = row2index["category E"]

        data = list(map(lambda x: [x[d], x[f], x[i], x[e]], rows[1:]))

        result = {}

        for i in data:
            if i[0] not in result:
                result[i[0]] = i
            break

        for key, category in result.items():
            c = Category()
            c.translations.append(CategoryTranslation(
                languageCode=LanguageCode.GERMAN, name=category[0]))
            c.translations.append(CategoryTranslation(
                languageCode=LanguageCode.FRENCH, name=category[1]))
            c.translations.append(CategoryTranslation(
                languageCode=LanguageCode.ITALIAN, name=category[2]))
            c.translations.append(CategoryTranslation(
                languageCode=LanguageCode.ENGLISH, name=category[3]))
            db_session.add(c)
        db_session.commit()
        print("Import categories done!")

