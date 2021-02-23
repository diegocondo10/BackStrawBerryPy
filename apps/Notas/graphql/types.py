import graphene
from graphene_django import DjangoObjectType

from apps.Notas.models import Componente, NotaAlumno, EvidenciaNotaAlumno


class ComponenteType(DjangoObjectType):
    class Meta:
        model = Componente


class EvidenciaNotaAlumnoType(DjangoObjectType):
    class Meta:
        model = EvidenciaNotaAlumno


class NotaAlumnoType(DjangoObjectType):
    # evidencias = graphene.List(EvidenciaNotaAlumno)

    class Meta:
        model = NotaAlumno
        # filter_fields = ["alumno_aula__id"]
        # interfaces = (relay.Node,)
    #
    # def resolve_evidencias(self: NotaAlumno, info):
    #     return EvidenciaNotaAlumno.objects.select_related("evidencias")
