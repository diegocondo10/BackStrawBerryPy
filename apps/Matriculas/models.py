from django.db import models

from BackStrawBerryPy.models import BaseModel
from apps.Personas.models import Personal, Alumno


# Create your models here.


class PeriodoLectivo(BaseModel):
    class EstadosPeriodo(models.IntegerChoices):
        CERRADO = 0
        ABIERTO = 1

    nombre = models.CharField(max_length=155)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.PositiveSmallIntegerField(default=1, choices=EstadosPeriodo.choices)
    fecha_fin_clases = models.DateField()
    observaciones = models.TextField(null=True, blank=True)

    coordinador = models.ForeignKey(Personal, on_delete=models.RESTRICT, related_name='coordinador', null=True)
    sub_coordinador = models.ForeignKey(Personal, on_delete=models.RESTRICT, related_name='sub_coordinador', null=True)
    director = models.ForeignKey(Personal, on_delete=models.RESTRICT, related_name='director', null=True)

    class Meta:
        db_table = 'PeriodoLectivos'


class Aula(BaseModel):
    nombre = models.CharField(max_length=50)
    capacidad = models.PositiveSmallIntegerField()
    grado = models.PositiveSmallIntegerField()
    alumnos = models.ManyToManyField(Alumno, through='AlumnoAula', blank=True)
    docentes = models.ManyToManyField(Personal)
    periodo = models.ForeignKey(PeriodoLectivo, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)
    jornada = models.CharField(max_length=50, default='MATUTINA')

    class Meta:
        db_table = 'Aulas'


# MATRICULA
class AlumnoAula(BaseModel):
    class EstadosMatricula(models.IntegerChoices):
        CREADA = 0
        ANULADA = 1
        FINALIZADA = 2

    diagnostico_clinico = models.TextField(null=True, blank=True)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    numero_matricula = models.CharField(max_length=155, default='', unique=True)
    matricula = models.TextField(null=True, blank=True)
    aporte_voluntario = models.DecimalField(decimal_places=2, max_digits=6)
    tratamiento = models.TextField(null=True, blank=True)

    total_faltas = models.PositiveSmallIntegerField(default=0)

    diagnostico_final = models.TextField(null=True, blank=True)

    motivo_anulacion = models.TextField(null=True, blank=True)

    estado_matricula = models.PositiveSmallIntegerField(
        default=EstadosMatricula.CREADA.value,
        choices=EstadosMatricula.choices
    )

    def generar_numero_matricula(self):
        return f'M-{self.pk}{self.alumno.id}{self.aula.pk}{self.alumno.persona.pk}'

    def verificar_matricula_creada(self):
        return False

    def save(self, *args, **kwargs):
        is_nueva = self.pk is None
        matricula = super(AlumnoAula, self).save(*args, **kwargs)

        if is_nueva:
            self.numero_matricula = self.generar_numero_matricula()
            self.matricula = self.numero_matricula
            self.save()

        return matricula

    class Meta:
        db_table = 'AlumnoAulas'


class Falta(BaseModel):
    alumno = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField(null=True)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'FaltasAlumno'
