from django.contrib.postgres.fields import JSONField
from django.db import models

# Create your models here.
from Auth.models import BaseModel


class Parametros(BaseModel):
    codigo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    value = JSONField()
