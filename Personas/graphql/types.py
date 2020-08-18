from graphene_django import DjangoObjectType

from Personas.models import Persona, Docente


class PersonaType(DjangoObjectType):
    class Meta:
        model = Persona


class DocenteType(DjangoObjectType):
    class Meta:
        model = Docente
