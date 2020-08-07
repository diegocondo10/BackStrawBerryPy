from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_estado = models.CharField(max_length=10, default='A')

    class Meta:
        abstract = True


class Aplicacion(BaseModel):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)


class Permiso(BaseModel):
    nombre = models.CharField(max_length=120)
    descripcion = models.TextField(null=True, blank=True)
    aplicacion = models.ForeignKey(Aplicacion, on_delete=models.CASCADE)


class Grupo(BaseModel):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    permisos = models.ManyToManyField(Permiso)


class Usuario(AbstractUser):
    email = models.EmailField()
    grupos = models.ManyToManyField(Grupo)
    permisos = models.ManyToManyField(Permiso)

    USERNAME_FIELD = "username"
