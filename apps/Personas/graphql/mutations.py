import graphene
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from apps.Personas.graphql.inputs import PadreDeFamiliaInput
from apps.Personas.models import Persona, Discapacidad, Alumno, Personal


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


class CreatePersonalMutation(DjangoCreateMutation):
    class Meta:
        model = Personal

    def after_mutate(cls, root, info, obj, return_data):
        return super(CreatePersonalMutation, cls).after_mutate(root, info, obj, return_data)


class UpdatePersonalMutation(DjangoUpdateMutation):
    class Meta:
        model = Personal


class DeletePersonalMutation(DjangoDeleteMutation):
    class Meta:
        model = Personal


class CreateAlumnoMutation(DjangoCreateMutation):
    class Meta:
        model = Alumno
        field_types = {
            "padre": graphene.Field(PadreDeFamiliaInput),
            "madre": graphene.InputField(PadreDeFamiliaInput),
            "representante": graphene.InputField(PadreDeFamiliaInput),
            "contacto_emergencia": graphene.InputField(PadreDeFamiliaInput),
        }


class UpdateAlumnoMutation(DjangoUpdateMutation):
    class Meta:
        model = Alumno
        field_types = {
            "padre": graphene.InputField(PadreDeFamiliaInput),
            "madre": graphene.InputField(PadreDeFamiliaInput),
            "representante": graphene.InputField(PadreDeFamiliaInput),
            "contacto_emergencia": graphene.InputField(PadreDeFamiliaInput),
        }


class DeleteAlumnoMutation(DjangoDeleteMutation):
    class Meta:
        model = Alumno
