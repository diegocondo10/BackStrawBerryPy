import graphene
from graphene_django.debug import DjangoDebug

from Auth.graphql.queries import AuthQueries
from Auth.schema import AuthMutations
from Matriculas.graphql.queries import MatriculasQueries
from Matriculas.schema import MatriculasMutations
from Personas.graphql.queries import PersonasQueries
from Personas.schema import PersonasMutations


class RootQueries(AuthQueries, PersonasQueries, MatriculasQueries, graphene.ObjectType, ):
    debug = graphene.Field(DjangoDebug, name='_debug')

    class Meta:
        description = 'Consultas disponibles'


class RootMutation(
    AuthMutations,
    PersonasMutations,
    MatriculasMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(query=RootQueries, mutation=RootMutation)
