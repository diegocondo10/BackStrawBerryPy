import graphene

from apps.Utils.models import Imagen
from apps.Utils.types import ImagenType


class UtilsQueries(graphene.ObjectType):
    imagenes = graphene.List(ImagenType)

    def resolve_imagenes(self, info):
        return Imagen.objects.all()
