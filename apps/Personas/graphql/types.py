import graphene
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType

from apps.Personas.graphql.interfaces import PadreDeFamiliaInterface
from apps.Personas.models import Persona, Discapacidad, Alumno, Personal, FuncionPersonal


class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad


class FuncionPersonalType(DjangoObjectType):
    class Meta:
        model = FuncionPersonal


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


class PersonalType(DjangoObjectType):
    funcion_str = graphene.String()
    info = GenericScalar()
    persona_str = graphene.String()

    class Meta:
        model = Personal

    def resolve_funcion_str(self: Personal, info):
        return self.funcion.nombre

    def resolve_persona_str(self: Personal, info):
        return self.persona.__str__()


class AlumnoType(DjangoObjectType):
    padre = graphene.Field(PadreDeFamiliaType)
    madre = graphene.Field(PadreDeFamiliaType)
    representante = graphene.Field(PadreDeFamiliaType)
    contacto_emergencia = graphene.Field(PadreDeFamiliaType)
    test = GenericScalar()

    class Meta:
        model = Alumno

    def resolve_padre(self, info):
        return self.padre

    def resolve_madre(self, info):
        return self.madre

    def resolve_representante(self, info):
        return self.representante
