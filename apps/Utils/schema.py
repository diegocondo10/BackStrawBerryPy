import graphene

from apps.Utils.mutations import SubirImagenMutation


class UtilsMutations(graphene.ObjectType):
    subir_imagen = SubirImagenMutation.Field()
