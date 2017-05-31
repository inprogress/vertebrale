import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from vertebrale.models import Food as FoodModel
from vertebrale.models import Category as CategoryModel
from vertebrale.models import CategoryTranslation
from vertebrale.models import LanguageCode
from vertebrale.database import db_session

class Food(SQLAlchemyObjectType):
    class Meta:
        model = FoodModel

class Category(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

class Query(graphene.ObjectType):
    foods = graphene.List(Food, name=graphene.String())
    categories = graphene.List(Category, language=graphene.String())

    def resolve_foods(self, args, context, info):
        query = Food.get_query(context)
        nameFilter = args.get('name')
        if nameFilter:
            return query.filter(FoodModel.name.like(nameFilter+"%")).all()
        return query.all()
    
    def resolve_categories(self, args, context, info):
        lc = LanguageCode.GERMAN
        lcFilter = args.get('language')
        if lcFilter:
            if lcFilter == 'fr':
                lc = LanguageCode.FRENCH
            if lcFilter == 'en':
                lc = LanguageCode.ENGLISH
            if lcFilter == 'it':
                lc = LanguageCode.ITALIAN
        return db_session.query(CategoryModel.id, CategoryTranslation.name).filter(CategoryTranslation.languageCode == lc).all()

schema = graphene.Schema(query=Query, types=[Food, Category])
