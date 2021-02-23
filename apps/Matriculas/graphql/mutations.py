import graphene
from django.db.models import QuerySet
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from apps.Matriculas.graphql.types import PeriodoLectivoType
from apps.Matriculas.models import PeriodoLectivo, Aula, AlumnoAula
from apps.common.graphql.types import ErrorType


class CreatePeriodoLectivoMutation(DjangoCreateMutation):
    class Meta:
        model = PeriodoLectivo


class UpdatePeriodoLectivoMutation(DjangoUpdateMutation):
    class Meta:
        model = PeriodoLectivo


class DeletePeriodoLectivoMutation(DjangoDeleteMutation):
    class Meta:
        model = PeriodoLectivo


class CerrarPeriodoLectivoMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True, description="ID de periodo lectivo")

    ok = graphene.Boolean()
    periodo = graphene.Field(PeriodoLectivoType)
    error = graphene.Field(ErrorType)

    @classmethod
    def mutate(cls, root, info, id):

        try:

            periodo: PeriodoLectivo = PeriodoLectivo.objects.get(
                pk=id,
                estado=PeriodoLectivo.EstadosPeriodo.ABIERTO.value
            )

            periodo.estado = PeriodoLectivo.EstadosPeriodo.CERRADO.value
            periodo.save()
            matriculas: QuerySet[AlumnoAula] = AlumnoAula.objects.filter(
                aula__periodo=periodo,
                estado_matricula=AlumnoAula.EstadosMatricula.CREADA.value
            )

            for matricula in matriculas:
                matricula.estado_matricula = AlumnoAula.EstadosMatricula.FINALIZADA.value

            AlumnoAula.objects.bulk_update(matriculas, ['estado_matricula'])

            return CerrarPeriodoLectivoMutation(ok=True, periodo=periodo)

        except PeriodoLectivo.DoesNotExist:

            return CerrarPeriodoLectivoMutation(
                ok=False,
                error=ErrorType(codigo=404, mensaje="No se ha encontrado ningún periodo lectivo abierto con ese ID")
            )


class CreateAulaMutation(DjangoCreateMutation):
    class Meta:
        model = Aula


class UpdateAulaMutation(DjangoUpdateMutation):
    class Meta:
        model = Aula


class DeleteAulaMutation(DjangoDeleteMutation):
    class Meta:
        model = Aula


class CreateAlumnoAulaMutation(DjangoCreateMutation):
    class Meta:
        model = AlumnoAula

    @classmethod
    def after_mutate(cls, root, info, obj: AlumnoAula, return_data):
        return super().after_mutate(root, info, obj, return_data)


class UpdateAlumnoAulaMutation(DjangoUpdateMutation):
    class Meta:
        model = AlumnoAula

    @classmethod
    def after_mutate(cls, root, info, obj: AlumnoAula, return_data):
        return super().after_mutate(root, info, obj, return_data)


class DeleteAlumnoAulaMutation(DjangoDeleteMutation):
    class Meta:
        model = AlumnoAula
