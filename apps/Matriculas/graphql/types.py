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
    class Meta:
        model = AlumnoAula
