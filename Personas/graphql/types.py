import graphene
from graphene_django import DjangoObjectType

from Personas.models import Persona, Discapacidad


class PersonaType(DjangoObjectType):
    full_name = graphene.String()
    str = graphene.String()

    class Meta:
        model = Persona
        exclude = ('extras',)

    def resolve_full_name(self: Persona, info, **kwargs):
        return self.full_name()

    def resolve_str(self: Persona, info, **kwargs):
        return self.__str__()


class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad
