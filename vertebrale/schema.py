import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from vertebrale.models import Food as FoodModel
from vertebrale.models import Category as CategoryModel
from vertebrale.database import db_session

class Food(SQLAlchemyObjectType):
    class Meta:
        model = FoodModel

class Category(SQLAlchemyObjectType):
    class Meta:
        model = CategoryModel

class Query(graphene.ObjectType):
    foods = graphene.List(Food, name=graphene.String())
    categories = graphene.List(Category)

    def resolve_foods(self, args, context, info):
        query = Food.get_query(context)
        nameFilter = args.get('name')
        if nameFilter:
            return query.filter(FoodModel.name.like(nameFilter+"%")).all()
        return query.all()
    
    def resolve_categories(self, args, context, info):
        query = Category.get_query(context)
        return query.all()

schema = graphene.Schema(query=Query, types=[Food, Category])
