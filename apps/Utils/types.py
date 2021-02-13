import graphene
from graphene_django import DjangoObjectType

from apps.Utils.models import Imagen


class ImagenType(DjangoObjectType):
    full_path = graphene.String()

    class Meta:
        model = Imagen

    def resolve_full_path(self: Imagen, info):
        return self.file.url
