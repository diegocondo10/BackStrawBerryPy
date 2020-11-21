import graphene

from apps.Personas.graphql.interfaces import PadreDeFamiliaInterface


class PadreDeFamiliaInput(graphene.InputObjectType, PadreDeFamiliaInterface):
    pass
