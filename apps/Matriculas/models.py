from django.db import models

from BackStrawBerryPy.models import BaseModel
from apps.Personas.models import Personal, Alumno


# Create your models here.


class PeriodoLectivo(BaseModel):
    nombre = models.CharField(max_length=155)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.CharField(max_length=30)
    fecha_fin_clases = models.DateField()
    observaciones = models.TextField(null=True, blank=True)
    responsables = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'PeriodoLectivos'


class Aula(BaseModel):
    nombre = models.CharField(max_length=50)
    # numero = models.PositiveSmallIntegerField(null=True)
    # TODO: averiguar si tiene jornada
    capacidad = models.PositiveSmallIntegerField()
    grado = models.PositiveSmallIntegerField()
    alumnos = models.ManyToManyField(Alumno, through='AlumnoAula', blank=True)
    docentes = models.ManyToManyField(Personal)
    periodo = models.ForeignKey(PeriodoLectivo, on_delete=models.CASCADE)
    observaciones = models.TextField(null=True, blank=True)
    jornada = models.CharField(max_length=50, default='MATUTINA')

    class Meta:
        db_table = 'Aulas'


class Materia(BaseModel):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    grado = models.PositiveSmallIntegerField()
    horas_presencial = models.PositiveSmallIntegerField()
    descripcion = models.TextField(null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    objetivo_especifico = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Materias'


# MATRICULA
class AlumnoAula(BaseModel):

    def default_info_faltas(self):
        return dict(total_faltas=0, faltas=[])

    diagnostico_clinico = models.TextField(null=True, blank=True)

    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    numero_matricula = models.CharField(max_length=155, default='')
    matricula = models.TextField(null=True, blank=True)
    aporte_voluntario = models.DecimalField(decimal_places=2, max_digits=6)
    tratamiento = models.TextField(null=True, blank=True)
    info_faltas = models.JSONField(default=default_info_faltas)
    diagnostico_final = models.TextField(null=True, blank=True)

    # lambda: dict(total_faltas=0, faltas=[])

    def generar_matricula(self):
        pass

    '''
        PREGUNTAS:
            - En caso de retirarce del IPCA que ocurre con la matricula?
    '''

    class Meta:
        db_table = 'AlumnoAulas'


class NotaAlumno(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)

    class Meta:
        db_table = 'NotaAlumnos'


# MallaAlumno
'''
class NotaMateria(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    observaciones = models.TextField(null=True, blank=True)
    materia = models.JSONField()
    # materia_fk = models.ForeignKey(Materia, on_delete=models.CASCADE)
    notas = models.JSONField(null=True, blank=True)

    
        PREGUNTAS:
            - Formato de notas?
            - Tipos de reportes que necesitan?
            - Tienen minimos y maximo?
            
        matematica:
            valorFinal: 100,
            notas:[
                {
                    titulo:'Paseo1'
                    valor:10
                    fechaRegistro:2020-10-12-08:00:45,
                    descripcion:'COMENTARIOS DOCENTE',
                    usuario: objUser
                }
            ]
            

    class Meta:
        db_table = 'NotaMateria'
'''
