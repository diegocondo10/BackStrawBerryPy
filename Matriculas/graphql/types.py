import graphene
from graphene_django import DjangoObjectType

from Matriculas.models import PeriodoLectivo, Aula, Materia,  AlumnoAula, NotaMateria


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


class NotaMateriaType(DjangoObjectType):
    class Meta:
        model = NotaMateria
