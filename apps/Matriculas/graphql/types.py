import graphene
from graphene_django import DjangoObjectType

from apps.Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula

EstadosMatriculaEnum = graphene.Enum.from_enum(AlumnoAula.EstadosMatricula, description='Estado de una matricula')


class PeriodoLectivoType(DjangoObjectType):
    estado = graphene.String(show_as=graphene.String(default_value="label"))
    matriculas = graphene.List(lambda: AlumnoAulaType, estados=graphene.List(EstadosMatriculaEnum, default_value=[]))
    numero_matriculas = graphene.Int(estados=graphene.List(EstadosMatriculaEnum, default_value=[]))
    habilitar_cierre = graphene.Boolean()

    class Meta:
        model = PeriodoLectivo

    def resolve_estado(self: PeriodoLectivo, info, show_as):
        if show_as == 'label':
            return self.get_estado_display().upper()
        return self.estado

    def resolve_matriculas(self: PeriodoLectivo, info, estados: list):
        if self is not None:
            if estados is None or estados.__len__() == 0:
                return AlumnoAula.objects.filter(aula__periodo=self)
            else:
                return AlumnoAula.objects.filter(aula__periodo=self, estado_matricula__in=estados)
        return None

    def resolve_habilitar_cierre(self: PeriodoLectivo, info):
        return self.estado == PeriodoLectivo.EstadosPeriodo.ABIERTO

    def resolve_numero_matriculas(self: PeriodoLectivo, info, estados):
        if self is not None:
            if estados is None or estados.__len__() == 0:
                return AlumnoAula.objects.filter(aula__periodo=self).count()
            else:
                return AlumnoAula.objects.filter(aula__periodo=self, estado_matricula__in=estados).count()
        return None


class AulaType(DjangoObjectType):
    class Meta:
        model = Aula


class MateriaType(DjangoObjectType):
    class Meta:
        model = Materia


class AlumnoAulaType(DjangoObjectType):
    estado_matricula = graphene.String()

    class Meta:
        model = AlumnoAula

    def resolve_estado_matricula(self: AlumnoAula, info):
        return self.get_estado_matricula_display()
