from django.db import models

# Create your models here.
from BackStrawBerryPy.models import BaseModel
from apps.Matriculas.models import AlumnoAula


class Componente(BaseModel):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Componente'


class NotaAlumno(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)
    componentes = models.JSONField(null=True, blank=True)
    resultado = models.CharField(max_length=150, null=True, blank=True)
    observaciones = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "NotasAlumno"
