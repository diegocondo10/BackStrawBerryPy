import graphene
from graphene_django.debug import DjangoDebug

from Auth.graphql.queries import AuthQueries


class RootQueries(AuthQueries, graphene.ObjectType, ):
    debug = graphene.Field(DjangoDebug, name='_debug')

    class Meta:
        description = 'Consultas disponibles'


schema = graphene.Schema(query=RootQueries)
