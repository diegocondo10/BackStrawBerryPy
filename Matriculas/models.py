from django.contrib.postgres.fields import JSONField
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
    responsables = JSONField(null=True, blank=True)
    '''
        PREGUNTAS:
            - Si hay responsables por periodo lectivo y cuantos son?
        
    '''

    class Meta:
        db_table = 'PeriodoLectivo'


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
    jornada = models.CharField(max_length=50, default='MATUTINA')

    '''
        PREGUNTAS:
            - Tiene mas de una jornada?
            - Cuanto docentes por aula?
            - Los docentes dan la misma materia?
    '''

    class Meta:
        db_table = 'Aula'


class Materia(BaseModel):
    nombre = models.CharField(max_length=50)
    codigo = models.CharField(max_length=20)
    grado = models.PositiveSmallIntegerField()
    horas_presencial = models.PositiveSmallIntegerField()
    descripcion = models.TextField(null=True, blank=True)
    objetivo = models.TextField(null=True, blank=True)
    objetivo_especifico = models.TextField(null=True, blank=True)

    '''
        PREGUNTAS:
            - Informes que mandan al ministerior de educacion cuales? y formatos.
                -  Malla de Alumnos?
            
    '''

    class Meta:
        db_table = 'Materia'


# MATRICULA
class AlumnoAula(BaseModel):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    nota_final = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    numero_faltas = models.PositiveSmallIntegerField(default=0)
    tratamiento = models.TextField()
    diagnostico = models.TextField()
    matricula = models.TextField()
    numero_matricula = models.CharField(max_length=155, default='')
    aporte_voluntario = models.DecimalField(decimal_places=2, max_digits=6)
    diagnostico_final = models.TextField(null=True, blank=True)
    faltas = JSONField(default=[])

    def generar_matricula(self):
        materias = Materia.objects.filter(grado=self.aula.grado)
        for materia in materias:
            nota_materia = NotaMateria()
            nota_materia.alumno_aula_id = self.pk
            nota_materia.notas = []
            nota_materia.materia = materia.__to_json__()
            nota_materia.save()

    '''
        PREGUNTAS:
            - Pierden el anio?
                - Causas de perdida de anio?
                - Numero maximo de matriculas?
                - Motivos para perder el anio? 
            
            - Calculo para nota final(de todas las materias)
            - Maximo de numero de faltas
            - En caso de retirarce del IPCA que ocurre con la matricula?
        
        [
            {
                fecha: 2020-10-15,
                horaInicio?: 08:00,
                horaFin?: 10:00,
                justificacion: "COMENTARIO DEL PADRE DE FAMILIA",
                comentarios: "COMENTARIO DEL DOCENTE"   
                usuario: obj             
            }
        ]
            - Confirmar que la falta es por dia y no por horas.
            
        
    '''

    class Meta:
        db_table = 'AlumnoAula'


# MallaAlumno
class NotaMateria(BaseModel):
    alumno_aula = models.ForeignKey(AlumnoAula, on_delete=models.CASCADE)
    valor = models.DecimalField(decimal_places=2, max_digits=6, default=0)
    observaciones = models.TextField(null=True, blank=True)
    materia = JSONField()
    # materia_fk = models.ForeignKey(Materia, on_delete=models.CASCADE)
    notas = JSONField(default={})

    '''
    
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
            
    '''

    class Meta:
        db_table = 'NotaMateria'
