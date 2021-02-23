import graphene

from apps.Matriculas.graphql.types import PeriodoLectivoType, AulaType, MateriaType, AlumnoAulaType, \
    EstadosPeriodoLectivoEnum
from apps.Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula


class MatriculasQueries(graphene.ObjectType):
    periodos_lectivos = graphene.List(
        PeriodoLectivoType,
        estados=graphene.List(EstadosPeriodoLectivoEnum, default_value=[])
    )
    periodo_lectivo = graphene.Field(PeriodoLectivoType, id=graphene.ID(required=True))

    aulas = graphene.List(AulaType)
    aulas_periodo_abierto = graphene.List(AulaType)
    aula = graphene.Field(AulaType, id=graphene.ID(required=True))

    materias = graphene.List(MateriaType)
    materia = graphene.Field(MateriaType, id=graphene.ID(required=True))

    matriculas = graphene.List(AlumnoAulaType)
    matricula = graphene.Field(AlumnoAulaType, id=graphene.ID(required=True))

    def resolve_periodo_lectivo(self, info, id):
        return PeriodoLectivo.objects.filter(pk=id).first()

    def resolve_periodos_lectivos(self, info, estados: list):
        if estados.__len__() == 0:
            return PeriodoLectivo.objects.all()
        return PeriodoLectivo.objects.filter(estado__in=estados)

    def resolve_aula(self, info, id):
        return Aula.objects.filter(pk=id).first()

    def resolve_aulas(self, info, **kwargs):
        return Aula.objects.all()

    def resolve_aulas_periodo_abierto(self, info, **kwargs):
        return Aula.objects.filter(periodo__estado=PeriodoLectivo.EstadosPeriodo.ABIERTO)

    def resolve_materia(self, info, id):
        return Materia.objects.filter(pk=id).first()

    def resolve_materias(self, info, **kwargs):
        return Materia.objects.all()

    def resolve_matriculas(self, info, **kwargs):
        return AlumnoAula.objects.all()

    def resolve_matricula(self, info, id):
        return AlumnoAula.objects.filter(pk=id).first()
