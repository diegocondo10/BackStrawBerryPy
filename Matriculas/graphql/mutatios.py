from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from Matriculas.models import PeriodoLectivo, Aula, Materia


class CreatePeriodoLectivoMutation(DjangoCreateMutation):
    class Meta:
        model = PeriodoLectivo


class UpdatePeriodoLectivoMutation(DjangoUpdateMutation):
    class Meta:
        model = PeriodoLectivo


class DeletePeriodoLectivoMutation(DjangoDeleteMutation):
    class Meta:
        model = PeriodoLectivo


class CreateAulaMutation(DjangoCreateMutation):
    class Meta:
        model = Aula


class UpdateAulaMutation(DjangoUpdateMutation):
    class Meta:
        model = Aula


class DeleteAulaMutation(DjangoDeleteMutation):
    class Meta:
        model = Aula


class CreateMateriaMutation(DjangoCreateMutation):
    class Meta:
        model = Materia


class UpdateMateriaMutation(DjangoUpdateMutation):
    class Meta:
        model = Materia


class DeleteMateriaMutation(DjangoDeleteMutation):
    class Meta:
        model = Materia
