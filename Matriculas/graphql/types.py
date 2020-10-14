from graphene_django import DjangoObjectType

from Matriculas.models import PeriodoLectivo, Aula, Materia


class PeriodoLectivoType(DjangoObjectType):
    class Meta:
        model = PeriodoLectivo


class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia
