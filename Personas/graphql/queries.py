import graphene
import graphene_django

from Personas.graphql.types import PersonaType, DiscapacidadType
from Personas.models import Persona, Discapacidad


class PersonasQueries(graphene.ObjectType):
    personas = graphene.List(PersonaType)
    persona = graphene.Field(PersonaType, id=graphene.ID(required=True))

    discapacidades = graphene.List(DiscapacidadType)
    discapacidad = graphene.Field(DiscapacidadType, id=graphene.ID(required=True))

    def resolve_personas(self, info, **kwargs):
        return Persona.objects.all().order_by("id")

    def resolve_persona(self,info, **kwargs):
        return Persona.objects.filter(id=id).first()

    def resolve_discapacidades(self, info, **kwargs):
        return Discapacidad.objects.all()

    def resolve_discapacidad(self, info, id):
        return Discapacidad.objects.filter(pk=id).first()
