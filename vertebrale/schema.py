import graphene
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models import Food as FoodModel

class Food(SQLAlchemyObjectType):
    class Meta:
        model = FoodModel

class Query(graphene.ObjectType):
    foods = graphene.List(Food, name=graphene.String())

    def resolve_foods(self, args, context, info):
        query = Food.get_query(context)
        nameFilter = args.get('name')
        if nameFilter:
            return query.filter(FoodModel.name.like(nameFilter+"%")).all()
        return query.all()

schema = graphene.Schema(query=Query, types=[Food])
