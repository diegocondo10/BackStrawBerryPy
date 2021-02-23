import graphene
from graphene_django import DjangoListField

from BackStrawBerryPy.models import BaseModel
from apps.Notas.graphql.types import ComponenteType, NotaAlumnoType
from apps.Notas.models import NotaAlumno


class NotasQueries(graphene.ObjectType):
    componentes = DjangoListField(ComponenteType)

    # notas_alumno = DjangoFilterConnectionField(NotaAlumnoType, )
    notas_alumnos = DjangoListField(NotaAlumnoType)
    notas_alumno = DjangoListField(NotaAlumnoType, id_alumo=graphene.ID(required=True))

    def resolve_notas_alumno(self, info, id_alumo):
        return NotaAlumno.objects.filter(alumno_aula__id=id_alumo, auth_estado=BaseModel.ACTIVO)

    def resolve_notas_alumnos(self, info):
        return NotaAlumno.objects.filter(auth_estado=BaseModel.ACTIVO)
