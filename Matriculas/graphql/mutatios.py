import json

from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from Matriculas.models import PeriodoLectivo, Aula, Materia, AlumnoAula, NotaMateria


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


class CreateAlumnoAulaMutation(DjangoCreateMutation):
    class Meta:
        model = AlumnoAula

    @classmethod
    def after_mutate(cls, root, info, obj: AlumnoAula, return_data):
        obj.crear_notas()
        return super().after_mutate(root, info, obj, return_data)


class UpdateAlumnoAulaMutation(DjangoUpdateMutation):
    class Meta:
        model = AlumnoAula


class DeleteAlumnoAulaMutation(DjangoDeleteMutation):
    class Meta:
        model = AlumnoAula


class CreateNotaMateria(DjangoCreateMutation):
    class Meta:
        model = NotaMateria


class UpdateNotaMateria(DjangoUpdateMutation):
    class Meta:
        model = NotaMateria


class DeleteNotaMateria(DjangoDeleteMutation):
    class Meta:
        model = NotaMateria