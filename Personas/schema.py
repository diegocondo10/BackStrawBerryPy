import graphene

from Personas.graphql.mutations import *


class PersonasMutations(graphene.ObjectType):
    create_persona = CreatePersonaMutation.Field()

    create_discapacidad = CreateDiscapacidadMutation.Field()
    update_discapacidad = UpdateDiscapacidadMutation.Field()
    delete_discapacidad = DeleteDiscapacidadMutation.Field()
