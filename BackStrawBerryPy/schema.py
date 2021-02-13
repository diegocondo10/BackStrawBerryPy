import graphene
from graphene_django.debug import DjangoDebug

from apps.Auth.graphql.queries import AuthQueries
from apps.Auth.schema import AuthMutations
from apps.Matriculas.graphql.queries import MatriculasQueries
from apps.Matriculas.schema import MatriculasMutations
from apps.Personas.graphql.queries import PersonasQueries
from apps.Personas.schema import PersonasMutations
from apps.Utils.queries import UtilsQueries
from apps.Utils.schema import UtilsMutations
from apps.Utils.types import ImagenType


class RootQueries(
    AuthQueries,
    PersonasQueries,
    MatriculasQueries,
    # MeQuery,
    UtilsQueries,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name='_debug')

    class Meta:
        description = 'Consultas disponibles'


class RootMutation(
    AuthMutations,
    PersonasMutations,
    MatriculasMutations,
    UtilsMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    # types=[ImagenType],
    query=RootQueries,
    mutation=RootMutation,
)
