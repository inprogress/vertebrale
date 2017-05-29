import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyConnectionField, SQLAlchemyObjectType

from models import Ingredient as IngredientModel

class Ingredient(SQLAlchemyObjectType):
    class Meta:
        model = IngredientModel
        interfaces = (relay.Node, )

class Query(graphene.ObjectType):
    ingredients = graphene.List(Ingredient, name=graphene.String())

    def resolve_ingredients(self, args, context, info):
        query = Ingredient.get_query(context)
        nameFilter = args.get('name')
        if nameFilter:
            return query.filter(IngredientModel.name.like(nameFilter+"%")).all()
        return query.all()

schema = graphene.Schema(query=Query, types=[Ingredient])
