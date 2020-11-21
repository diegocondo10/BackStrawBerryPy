import graphene
from graphene_django.debug import DjangoDebug

from apps.Auth.graphql.queries import AuthQueries
from apps.Auth.schema import AuthMutations
from apps.Matriculas.graphql.queries import MatriculasQueries
from apps.Matriculas.schema import MatriculasMutations
from apps.Personas.graphql.queries import PersonasQueries
from apps.Personas.schema import PersonasMutations


class RootQueries(
    AuthQueries,
    PersonasQueries,
    MatriculasQueries,
    graphene.ObjectType,
):
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
