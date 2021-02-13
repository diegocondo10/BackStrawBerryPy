from graphene_django_cud.mutations import DjangoCreateMutation
from graphene_file_upload.scalars import Upload

from apps.Utils.models import Imagen


class SubirImagenMutation(DjangoCreateMutation):
    class Meta:
        model = Imagen
        field_types = {
            'file': Upload()
        }
        required_fields = ("file",)
