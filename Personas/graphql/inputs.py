import graphene

from Personas.graphql.interfaces import PadreDeFamiliaInterface


class PadreDeFamiliaInput(graphene.InputObjectType, PadreDeFamiliaInterface):
    pass
