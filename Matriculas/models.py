from django.db import models

# Create your models here.
from BackStrawBerryPy.models import BaseModel
from Personas.models import Docente, Alumno


class PeriodoLectivo(BaseModel):
    nombre = models.CharField(max_length=155)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=30)
    fecha_fin_clases = models.DateField()
    observaciones = models.TextField(null=True, blank=True)
    responsables = models.ManyToManyField(Docente, through='ResponsablePeriodo')


class ResponsablePeriodo(BaseModel):
    periodo = models.ForeignKey(PeriodoLectivo, on_delete=models.CASCADE)
    responsable = models.ForeignKey(Docente, on_delete=models.CASCADE)
    rol = models.CharField(max_length=155)


class Aula(BaseModel):
    nombre = models.CharField(max_length=50)
    # numero = models.PositiveSmallIntegerField(null=True)
    # TODO: averiguar si tiene jornada
    capacidad = models.PositiveSmallIntegerField()
    grado = models.PositiveSmallIntegerField()
    estudiantes = models.ManyToManyField(Alumno, through='AlumnoAula', blank=True)
    docentes = models.ManyToManyField(Docente)
    periodo = models.ForeignKey(PeriodoLectivo, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)


class Materia(BaseModel):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    grado = models.PositiveSmallIntegerField()
    horas_presencial = models.TextField(null=True, blank=True)
    descripcion = models.CharField(max_length=50)
    objetivo = models.CharField(max_length=50)
    objetivo_especifico = models.CharField(max_length=50)


# MATRICULA
class AlumnoAula(BaseModel):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota_final = models.DecimalField(max_digits=6, decimal_places=2)
    numero_faltas = models.PositiveSmallIntegerField(default=0)
    notas = models.ManyToManyField('Nota', through='NotaEstudiante')
    tratamiento = models.TextField()
    diagnostico = models.TextField()
    matroicula = models.TextField()
    aporte_voluntario = models.DecimalField(decimal_places=2, max_digits=6)


class NotaEstudiante(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)
    nota = models.ForeignKey('Nota', on_delete=models.CASCADE)


class Nota(BaseModel):
    valor = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    observaciones = models.TextField(null=True, blank=True)
