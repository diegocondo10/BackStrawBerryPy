import graphene

from Matriculas.graphql.types import PeriodoLectivoType, AulaType, MateriaType, AlumnoAulaType
from Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula


class MatriculasQueries(graphene.ObjectType):
    periodos_lectivos = graphene.List(PeriodoLectivoType)
    periodo_lectivo = graphene.Field(PeriodoLectivoType, id=graphene.ID(required=True))

    aulas = graphene.List(AulaType)
    aula = graphene.Field(AulaType, id=graphene.ID(required=True))

    materias = graphene.List(MateriaType)
    materia = graphene.Field(MateriaType, id=graphene.ID(required=True))

    matriculas = graphene.List(AlumnoAulaType)
    matricula = graphene.Field(AlumnoAulaType, id=graphene.ID(required=True))

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

    def resolve_matriculas(self, info, **kwargs):
        return AlumnoAula.objects.all()

    def resolve_matricula(self, info, id):
        return AlumnoAula.objects.filter(pk=id)
