import graphene
from graphene_django import DjangoListField

from apps.Notas.graphql.types import ComponenteType, NotaAlumnoType
from apps.Notas.models import NotaAlumno


class NotasQueries(graphene.ObjectType):
    componentes = DjangoListField(ComponenteType)

    # notas_alumno = DjangoFilterConnectionField(NotaAlumnoType, )

    notas_alumno = DjangoListField(NotaAlumnoType, id_alumo=graphene.ID())

    def resolve_notas_alumno(self, info, id_alumo):
        return NotaAlumno.objects.filter(alumno_aula__id=id_alumo)
