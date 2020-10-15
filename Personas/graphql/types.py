from collections import namedtuple

import graphene
from graphene.types import unmountedtype
from graphene.types.unmountedtype import UnmountedType
from graphene_django import DjangoObjectType

from Personas.graphql.interfaces import PadreDeFamiliaInterface
from Personas.models import Persona, Discapacidad, Docente, Alumno


class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad


class PersonaType(DjangoObjectType):
    full_name = graphene.String(description='Nombre de la persona')
    str = graphene.String()
    discapacidades_disponibles = graphene.List(DiscapacidadType)
    representados = graphene.List(lambda: AlumnoType)

    class Meta:
        model = Persona
        exclude = ('extras',)

    def resolve_full_name(self: Persona, info, **kwargs):
        return self.full_name()

    def resolve_str(self: Persona, info, **kwargs):
        return self.__str__()

    def resolve_discapacidades_disponibles(self: Persona, info):
        return Discapacidad.objects.exclude(id__in=self.discapacidades.get_queryset().values_list('id'))


class PadreDeFamiliaType(graphene.ObjectType, PadreDeFamiliaInterface):
    pass


class DocenteType(DjangoObjectType):
    class Meta:
        model = Docente


class AlumnoType(DjangoObjectType):
    padre = graphene.Field(PadreDeFamiliaType)
    madre = graphene.Field(PadreDeFamiliaType)
    representante = graphene.Field(PadreDeFamiliaType)
    contacto_emergencia = graphene.Field(PadreDeFamiliaType)

    class Meta:
        model = Alumno

    def resolve_padre(self, info):
        return self.padre

    def resolve_madre(self, info):
        return self.madre

    def resolve_representante(self, info):
        return self.representante
