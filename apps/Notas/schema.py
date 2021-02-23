import graphene

from apps.Notas.graphql.mutations import *


class NotasMutations(graphene.ObjectType):
    create_nota = CreateNotaMutation.Field()
