import graphene
from graphene_django.debug import DjangoDebug

from Auth.graphql.queries import AuthQueries
from Auth.schema import AuthMutations
from Personas.graphql.queries import PersonasQueries
from Personas.schema import PersonasMutations


class RootQueries(AuthQueries, PersonasQueries, graphene.ObjectType, ):
    debug = graphene.Field(DjangoDebug, name='_debug')

    class Meta:
        description = 'Consultas disponibles'


class RootMutation(AuthMutations, PersonasMutations, graphene.ObjectType):
    pass


schema = graphene.Schema(query=RootQueries, mutation=RootMutation)
