import graphene
from graphene_django.debug import DjangoDebug

from apps.Auth.graphql.queries import AuthQueries
from apps.Auth.schema import AuthMutations
from apps.Matriculas.graphql.queries import MatriculasQueries
from apps.Matriculas.schema import MatriculasMutations
from apps.Notas.graphql.queries import NotasQueries
from apps.Notas.schema import NotasMutations
from apps.Personas.graphql.queries import PersonasQueries
from apps.Personas.reportes import reporte_nomina
from apps.Personas.schema import PersonasMutations
from apps.Utils.queries import UtilsQueries
from apps.Utils.schema import UtilsMutations


class RootQueries(
    AuthQueries,
    PersonasQueries,
    MatriculasQueries,
    # MeQuery,
    UtilsQueries,
    NotasQueries,
    graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name='_debug')

    get_reporte = graphene.String()

    def resolve_get_reporte(self, info, **kwargs):
        return reporte_nomina()

    class Meta:
        description = 'Consultas disponibles'


class RootMutation(
    AuthMutations,
    PersonasMutations,
    MatriculasMutations,
    UtilsMutations,
    NotasMutations,
    graphene.ObjectType
):
    pass


schema = graphene.Schema(
    # types=[ImagenType],
    query=RootQueries,
    mutation=RootMutation,
)
