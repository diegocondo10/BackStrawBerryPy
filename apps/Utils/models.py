import os
from uuid import uuid4

from django.db import models

# Create your models here.
from apps.Auth.models import BaseModel


def path_and_rename(instance, filename):
    instance.name = filename
    upload_to = instance.table
    ext = filename.split('.')[-1]

    new_name = f'{uuid4().hex}-{uuid4().hex}'
    filename = f'{new_name}.{ext}'
    new_path = os.path.join(upload_to, filename)
    return new_path


class Parametros(BaseModel):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    value = models.JSONField()


class Imagen(BaseModel):
    file = models.ImageField(upload_to=path_and_rename)
    name = models.CharField(max_length=255, null=True, blank=True)
    table = models.CharField(max_length=50, default="photos", db_index=True)

    class Meta:
        db_table = "Imagenes"
        # indexes = ('table',)
