from django.db import models

from BackStrawBerryPy.models import BaseModel


# Create your models here.

class FuncionPersonal(BaseModel):
    nombre = models.CharField()
    descripcion = models.TextField()

    class Meta:
        db_table = 'RolPersonal'


class Discapacidad(BaseModel):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'Discapacidad'


class Persona(BaseModel):
    identificacion = models.CharField(max_length=30, unique=True)
    tipo_identificacion = models.CharField(max_length=20, )
    primer_nombre = models.CharField(max_length=30)
    segundo_nombre = models.CharField(max_length=30)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)

    pais_nacimiento = models.CharField(max_length=30, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)

    genero = models.CharField(max_length=10, )
    estado_civil = models.CharField(max_length=20, null=True, blank=True)

    tiene_discapacidad = models.CharField(max_length=10, default="NO")
    discapacidades = models.ManyToManyField(Discapacidad, blank=True)
    carnet_conadis = models.CharField(max_length=50, default='NO REGISTRA')
    porcentaje_discapacidad = models.PositiveSmallIntegerField(default=0)

    etnia = models.CharField(max_length=30, )

    tipo_sangre = models.CharField(max_length=30, )

    pais_residencia = models.CharField(max_length=150)
    provincia_residencia = models.CharField(max_length=150)
    canton_residencia = models.CharField(max_length=150)
    parroquia_residencia = models.CharField(max_length=150)
    direccion_domiciliaria = models.TextField(null=True, blank=True)

    telefono = models.CharField(max_length=20, null=True, blank=True)
    celular_uno = models.CharField(max_length=20, null=True, blank=True)
    celular_dos = models.CharField(max_length=20, null=True, blank=True)

    correo = models.CharField(max_length=30, null=True, blank=True)

    foto = models.URLField(null=True, blank=True)
    extras = models.JSONField(null=True, blank=True)

    def full_name(self):
        return f'{self.primer_nombre} {self.primer_apellido}'

    def __str__(self):
        return f'{self.identificacion} {self.full_name()}'

    class Meta:
        db_table = 'Persona'


class Personal(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    funcion = models.ForeignKey(FuncionPersonal, on_delete=models.CASCADE)
    info = models.JSONField(null=True, blank=True)
    '''
    info:JSON
        {
         titulo_profesional
            
        }
    '''
    historico = models.JSONField(null=True, blank=True)

    class Meta:
        db_table = 'Personal'

    def full_name(self):
        return self.persona.full_name()

    def __str__(self):
        return self.persona.__str__()


class Alumno(BaseModel):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='alumno')

    padre = models.JSONField(null=True, blank=True)

    madre = models.JSONField(null=True, blank=True)

    representante = models.JSONField(null=True, blank=True)

    contacto_emergencia = models.JSONField(null=True, blank=True)

    observaciones = models.TextField(null=True, blank=True)

    historia_clinica = models.CharField(max_length=20, null=True, blank=True)

    trastornos_asociados = models.TextField(null=True, blank=True)

    grado_dependencia = models.TextField(null=True, blank=True)

    bono = models.CharField(max_length=50, default="Ninguno")
    tipo_bono = models.CharField(max_length=50)
    afiliacion_iess = models.CharField(max_length=10)
    quintil_pobreza = models.CharField(max_length=10)

    class Meta:
        db_table = 'Alumno'
