import graphene
from graphene_django import DjangoObjectType

from Personas.models import Persona, Discapacidad


class PersonaType(DjangoObjectType):
    full_name = graphene.String(description='Nombre de la persona')
    str = graphene.String()

    class Meta:
        model = Persona
        exclude = ('extras',)

    def resolve_full_name(self: Persona, info, **kwargs):
        return self.full_name()

    def resolve_str(self: Persona, info, **kwargs):
        return self.__str__()

    def resolve_discapacidades_disponibles(self: Persona, info):
        return Discapacidad.objects.exclude(id__in=self.discapacidades.get_queryset().values_list('id'))

class DiscapacidadType(DjangoObjectType):
    class Meta:
        model = Discapacidad
