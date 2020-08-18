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
        optional_fields = ('password',)

    @classmethod
    def after_mutate(cls, root, info, obj: Usuario, return_data):
        obj.password = '1234ABC'
        obj.set_password(obj.password)
        obj.save()
        return super().after_mutate(root, info, obj, return_data)


class UpdateUsuarioMutation(DjangoUpdateMutation):
    class Meta:
        model = Usuario
        optional_fields = ('password',)


class DeleteUsuarioMutation(DjangoDeleteMutation):
    class Meta:
        model = Usuario
