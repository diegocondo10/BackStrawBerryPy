from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation, DjangoDeleteMutation

from Auth.models import Aplicacion, Permiso, Grupo, Usuario


class CreateAplicacionMutation(DjangoCreateMutation):
    class Meta:
        model = Aplicacion


class UpdateAplicacionMutation(DjangoUpdateMutation):
    class Meta:
        model = Aplicacion


class DeleteAplicacionMutation(DjangoDeleteMutation):
    class Meta:
        model = Aplicacion


class CreatePermisoMutation(DjangoCreateMutation):
    class Meta:
        model = Permiso


class UpdatePermisoMutation(DjangoUpdateMutation):
    class Meta:
        model = Permiso


class DeletePermisoMutation(DjangoDeleteMutation):
    class Meta:
        model = Permiso


class CreateGrupoMutation(DjangoCreateMutation):
    class Meta:
        model = Grupo


class UpdateGrupoMutation(DjangoUpdateMutation):
    class Meta:
        model = Grupo


class DeleteGrupoMutation(DjangoDeleteMutation):
    class Meta:
        model = Grupo


class CreateUsuarioMutation(DjangoCreateMutation):
    class Meta:
        model = Usuario


class UpdateUsuarioMutation(DjangoUpdateMutation):
    class Meta:
        model = Usuario


class DeleteUsuarioMutation(DjangoDeleteMutation):
    class Meta:
        model = Usuario
