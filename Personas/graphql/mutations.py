import graphene
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from Personas.graphql.inputs import PadreDeFamiliaInput
from Personas.models import Persona, Discapacidad, Docente, Estudiante, PeriodoLectivo, Aula, Materia


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
        field_types = {
            "padre": graphene.InputField(PadreDeFamiliaInput),
            "madre": graphene.InputField(PadreDeFamiliaInput),
            "representante": graphene.InputField(PadreDeFamiliaInput),
            "contacto_emergencia": graphene.InputField(PadreDeFamiliaInput),
        }


class UpdateEstudianteMutation(DjangoUpdateMutation):
    class Meta:
        model = Estudiante
        field_types = {
            "padre": graphene.InputField(PadreDeFamiliaInput),
            "madre": graphene.InputField(PadreDeFamiliaInput),
            "representante": graphene.InputField(PadreDeFamiliaInput),
            "contacto_emergencia": graphene.InputField(PadreDeFamiliaInput),
        }


class DeleteEstudianteMutation(DjangoDeleteMutation):
    class Meta:
        model = Estudiante


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
