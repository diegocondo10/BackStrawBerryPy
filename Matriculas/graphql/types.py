import graphene
from graphene_django import DjangoObjectType

from Matriculas.models import PeriodoLectivo, Aula, Materia, ResponsablePeriodo, AlumnoAula, NotaMateria


class PeriodoLectivoType(DjangoObjectType):
    class Meta:
        model = PeriodoLectivo


class ResponsablePeriodoType(DjangoObjectType):
    class Meta:
        model = ResponsablePeriodo


class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia


class AlumnoAulaType(DjangoObjectType):
    class Meta:
        model = AlumnoAula


class NotaMateriaType(DjangoObjectType):
    class Meta:
        model = NotaMateria
