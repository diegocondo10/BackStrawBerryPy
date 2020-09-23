from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from Personas.models import Persona, Discapacidad, Docente, Estudiante, PeriodoLectivo, Aula


class CreatePersonaMutation(DjangoCreateMutation):
    class Meta:
        model = Persona
        exclude_fields = ('extras',)


class UpdatePersonaMutation(DjangoUpdateMutation):
    class Meta:
        model = Persona
        exclude_fields = ('extras',)


class DeletePersonaMutation(DjangoDeleteMutation):
    class Meta:
        model = Persona
        exclude_fields = ('extras',)


class CreateDiscapacidadMutation(DjangoCreateMutation):
    class Meta:
        model = Discapacidad


class UpdateDiscapacidadMutation(DjangoUpdateMutation):
    class Meta:
        model = Discapacidad


class DeleteDiscapacidadMutation(DjangoDeleteMutation):
    class Meta:
        model = Discapacidad


class CreateDocenteMutation(DjangoCreateMutation):
    class Meta:
        model = Docente


class UpdateDocenteMutation(DjangoUpdateMutation):
    class Meta:
        model = Docente


class DeleteDocenteMutation(DjangoDeleteMutation):
    class Meta:
        model = Docente


class CreateEstudianteMutation(DjangoCreateMutation):
    class Meta:
        model = Estudiante
        exclude_fields = ('extras',)


class UpdateEstudianteMutation(DjangoUpdateMutation):
    class Meta:
        model = Estudiante
        exclude_fields = ('extras',)


class DeleteEstudianteMutation(DjangoDeleteMutation):
    class Meta:
        model = Estudiante
        exclude_fields = ('extras',)

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