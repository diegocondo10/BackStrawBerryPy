import graphene

from Personas.graphql.types import PersonaType
from Personas.models import Persona


class PersonasQueries(graphene.ObjectType):
    personas = graphene.List(PersonaType)

    def resolve_personas(self, info, **kwargs):
        return Persona.objects.all()
