from django.db import models

# Create your models here.
from BackStrawBerryPy.models import BaseModel


class Discapacidad(BaseModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)
    porcentaje = models.PositiveSmallIntegerField(null=True)


class Persona(BaseModel):
    identificacion = models.CharField(max_length=30, unique=True)
    tipo_identificacion = models.CharField(max_length=20, )
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    genero = models.CharField(max_length=10, )
    sexo = models.CharField(max_length=10)
    # etnia = models.CharField(max_length=30, )
    foto = models.URLField(null=True, blank=True)
    # idioma = models.CharField(max_length=30, )
    tipo_sangre = models.CharField(max_length=30, )
    fecha_nacimiento = models.DateField(null=True, blank=True)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)
    # ubicacion = models.CharField()
    # nacionalidad = models.

    # RECIDENCIAS

    calle_principal = models.CharField(max_length=150, null=True, blank=True)
    calle_secundaria = models.CharField(max_length=150, null=True, blank=True)
    lugar_referencia = models.CharField(max_length=150, null=True, blank=True)
    numero_casa = models.CharField(max_length=30, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    celular = models.CharField(max_length=20, null=True, blank=True)
    correo = models.CharField(max_length=30, null=True, blank=True)

    # DISCAPACIDADES
    tiene_discapacidad = models.CharField(max_length=10, default="NO")
    discapacidades = models.ManyToManyField(Discapacidad, blank=True)
    carnet_conadis = models.CharField(max_length=50, default='NO REGISTRA')
    porcentaje_discapacidad = models.PositiveSmallIntegerField(default=0)

    ocupacion = models.CharField(max_length=120, null=True, blank=True)
    nivel_formacion = models.CharField(max_length=255, null=True, blank=True)
    extras = models.JSONField(null=True, blank=True)

    def full_name(self):
        return f'{self.primer_nombre} {self.primer_apellido}'

    def __str__(self):
        return f'{self.identificacion} {self.full_name()}'


class Docente(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    # titulo = models.CharField(max_length=120) NUEVO CRUD
    codigo = models.CharField(max_length=50, null=True, blank=True)
    tipo_titulo = models.CharField(max_length=120)
    titulo = models.CharField(max_length=255)
    observaciones = models.TextField(null=True, blank=True)


class Estudiante(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='persona_fk')
    padre = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='padre_fk')
    madre = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='madre_fk')
    representante = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='representante_fk')
    relacion_representante = models.CharField(max_length=100)

    # observaciones = models.TextField() dentro de extras
    extras = models.JSONField(null=True, blank=True)


'''

class Especialidad(BaseModel):
    nombre = models.CharField()
    descripcion = models.TextField()


class Terapeuta(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    especialidades = models.ManyToManyField(Especialidad)


class Pasante(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    nombre_institucion = models.CharField(max_length=100)
    especialidad = models.CharField(max_lenght=100)
    tutor = models.ForeignKey(Docente, on_delete=models.CASCADE)
    numero_horas_diarias = models.PositiveSmallIntegerField()



class Aula(BaseModel):
    espcialidades = models.ManyToManyField(Especialidad)
    terapeutas = models.ManyToManyField(Especialidad)
'''
