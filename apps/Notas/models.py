from django.db import models
# Create your models here.
from graphene import relay

from BackStrawBerryPy.models import BaseModel
from apps.Matriculas.models import AlumnoAula


class Componente(BaseModel):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Componentes'


class NotaAlumno(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE, related_name="alumno_aula")
    componente = models.ForeignKey(Componente, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=150)
    resultado = models.CharField(max_length=150, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "NotasAlumno"
