import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from Personas.models import Persona, Discapacidad, Docente, Estudiante, PeriodoLectivo, Aula, Materia


class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad


class PersonaType(DjangoObjectType):
    full_name = graphene.String(description='Nombre de la persona')
    str = graphene.String()
    discapacidades_disponibles = graphene.List(DiscapacidadType)
    representados = graphene.List(lambda: EstudianteType)

    class Meta:
        model = Persona
        exclude = ('extras',)

    def resolve_full_name(self: Persona, info, **kwargs):
        return self.full_name()

    def resolve_str(self: Persona, info, **kwargs):
        return self.__str__()

    def resolve_discapacidades_disponibles(self: Persona, info):
        return Discapacidad.objects.exclude(id__in=self.discapacidades.get_queryset().values_list('id'))

    def resolve_representados(self: Persona, info):
        return Estudiante.objects.filter(Q(padre__pk=self.id) | Q(madre__pk=self.id) | Q(representante__pk=self.id))


class DocenteType(DjangoObjectType):
    class Meta:
        model = Docente


class EstudianteType(DjangoObjectType):
    class Meta:
        model = Estudiante
        exclude = ('extras',)


class PeriodoLectivoType(DjangoObjectType):
    class Meta:
        model = PeriodoLectivo


class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia
