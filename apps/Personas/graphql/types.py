import datetime

import graphene
import moment
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType

from apps.Personas.graphql.interfaces import PadreDeFamiliaInterface
from apps.Personas.models import Persona, Discapacidad, Alumno, Personal, FuncionPersonal
from utils.functions import concat_if_exist


class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad


class FuncionPersonalType(DjangoObjectType):
    class Meta:
        model = FuncionPersonal


class PersonaType(DjangoObjectType):
    full_name = graphene.String(description='Nombre de la persona')
    edad = graphene.Int()
    str = graphene.String()
    discapacidades_disponibles = graphene.List(DiscapacidadType)
    # representados = graphene.List(lambda: AlumnoType)

    nombres = graphene.String()
    apellidos = graphene.String()

    class Meta:
        model = Persona
        exclude = ('extras',)

    def resolve_full_name(self: Persona, info, **kwargs):
        return self.full_name()

    def resolve_str(self: Persona, info, **kwargs):
        return self.__str__()

    def resolve_discapacidades_disponibles(self: Persona, info):
        return Discapacidad.objects.exclude(id__in=self.discapacidades.get_queryset().values_list('id'))

    def resolve_edad(self: Persona, info):
        now = datetime.date.today().strftime('%Y-%m-%d')
        moment_date = moment.date(now, 'YYYY-MM-DD').subtract(
            years=self.fecha_nacimiento.year,
            months=self.fecha_nacimiento.month,
            days=self.fecha_nacimiento.day
        )
        return moment_date.year

    def resolve_nombres(self: Persona, info):
        return self.get_nombres()

    def resolve_apellidos(self: Persona, info):
        return self.get_apellidos()


class PadreDeFamiliaType(graphene.ObjectType, PadreDeFamiliaInterface):
    nombres = graphene.String()
    apellidos = graphene.String()
    full_name = graphene.String()

    def resolve_nombres(self: dict, info):
        return concat_if_exist(self.get('primer_nombre'), self.get('segundo_nombre'))

    def resolve_apellidos(self: dict, info):
        return concat_if_exist(self.get('primer_apellido'), self.get('segundo_apellido'))

    def resolve_full_name(self: dict, info):
        return concat_if_exist(
            self.get('primer_apellido'), self.get('segundo_apellido'),
            self.get('primer_nombre'), self.get('segundo_nombre')
        )


class PersonalType(DjangoObjectType):
    info = GenericScalar()
    persona_str = graphene.String()

    class Meta:
        model = Personal

    def resolve_persona_str(self: Personal, info):
        return self.persona.__str__()


class AlumnoType(DjangoObjectType):
    padre = graphene.Field(PadreDeFamiliaType)
    madre = graphene.Field(PadreDeFamiliaType)
    representante = GenericScalar()
    contacto_emergencia = GenericScalar()
    test = GenericScalar()

    persona_str = graphene.String()

    class Meta:
        model = Alumno

    def resolve_padre(self, info):
        return self.padre

    def resolve_madre(self, info):
        return self.madre

    def resolve_representante(self, info):
        return self.representante

    def resolve_contacto_emergencia(self, info):
        return self.contacto_emergencia

    def resolve_persona_str(self: Alumno, info):
        return self.persona.__str__()
