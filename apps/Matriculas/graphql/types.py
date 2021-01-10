import graphene
from graphene_django import DjangoObjectType

from apps.Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula


class PeriodoLectivoType(DjangoObjectType):
    class Meta:
        model = PeriodoLectivo


class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia


class AlumnoAulaType(DjangoObjectType):
    estado_matricula = graphene.String()

    class Meta:
        model = AlumnoAula

    def resolve_estado_matricula(self: AlumnoAula, info):
        return self.get_estado_matricula_display()
