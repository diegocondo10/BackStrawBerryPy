import graphene
from graphql import GraphQLError
from graphql.error import GraphQLLocatedError
from graphql_auth.exceptions import GraphQLAuthError
from graphql_jwt.decorators import login_required

from Matriculas.graphql.types import PeriodoLectivoType, AulaType, MateriaType, AlumnoAulaType, NotaMateriaType
from Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula, NotaMateria


class MatriculasQueries(graphene.ObjectType):
    periodos_lectivos = graphene.List(PeriodoLectivoType)
    periodo_lectivo = graphene.Field(PeriodoLectivoType, id=graphene.ID(required=True))

    aulas = graphene.List(AulaType)
    aula = graphene.Field(AulaType, id=graphene.ID(required=True))

    materias = graphene.List(MateriaType)
    materia = graphene.Field(MateriaType, id=graphene.ID(required=True))

    matriculas = graphene.List(AlumnoAulaType)
    matricula = graphene.Field(AlumnoAulaType, id=graphene.ID(required=True))

    nota_materias = graphene.List(NotaMateriaType)
    nota_materia = graphene.Field(NotaMateriaType, id=graphene.ID(required=True))

    def resolve_periodo_lectivo(self, info, id):
        return PeriodoLectivo.objects.filter(pk=id).first()

    def resolve_periodos_lectivos(self, info, **kwargs):
        return PeriodoLectivo.objects.all()

    def resolve_aula(self, info, id):
        return Aula.objects.filter(pk=id).first()

    def resolve_aulas(self, info, **kwargs):
        return Aula.objects.all()

    def resolve_materia(self, info, id):
        return Materia.objects.filter(pk=id).first()

    def resolve_materias(self, info, **kwargs):
        return Materia.objects.all()

    # @login_required
    def resolve_matriculas(self, info, **kwargs):
        print(info)
        # return GraphQLError('ERROR', extensions={'test': 'prueba'})
        return AlumnoAula.objects.all()

    def resolve_matricula(self, info, id):
        return AlumnoAula.objects.filter(pk=id).first()

    def resolve_nota_materias(self, info, **kwargs):
        return NotaMateria.objects.all()

    def resolve_nota_materia(self, info, id):
        return NotaMateria.objects.filter(pk=id)
