from graphene_django import DjangoObjectType

from apps.Notas.models import Componente, NotaAlumno


class ComponenteType(DjangoObjectType):
    class Meta:
        model = Componente


class NotaAlumnoType(DjangoObjectType):
    class Meta:
        model = NotaAlumno
        # filter_fields = ["alumno_aula__id"]
        # interfaces = (relay.Node,)
