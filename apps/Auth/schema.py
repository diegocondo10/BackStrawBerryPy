import graphene
from graphql_auth import mutations
from graphql_auth.models import UserStatus
from graphql_auth.utils import revoke_user_refresh_token

from apps.Auth.graphql.mutations import *


class ChangePassword(mutations.PasswordChange):

    @classmethod
    # @password_confirmation_required
    def resolve_mutation(cls, root, info, **kwargs):
        user = info.context.user
        f = cls.form(user, kwargs)
        if f.is_valid():
            revoke_user_refresh_token(user)
            user = f.save()
            payload = cls.login_on_password_change(
                root,
                info,
                password=kwargs.get("new_password1"),
                **{user.USERNAME_FIELD: getattr(user, user.USERNAME_FIELD)}
            )
            return_value = {}
            for field in cls._meta.fields:
                return_value[field] = getattr(payload, field)
            return cls(**return_value)
        else:
            return cls(success=False, errors=f.errors.get_json_data())

    @classmethod
    def mutate(cls, root, info, **input):
        if info.context.user:
            UserStatus.objects.filter(user_id=info.context.user.id).update(verified=True)
        return super().mutate(root, info, **input)


class AuthMutations(graphene.ObjectType):
    create_permiso = CreatePermisoMutation.Field()
    update_permiso = UpdatePermisoMutation.Field()
    delete_permiso = DeletePermisoMutation.Field()

    create_grupo = CreateGrupoMutation.Field()
    update_grupo = UpdateGrupoMutation.Field()
    delete_grupo = DeleteGrupoMutation.Field()

    create_usuario = CreateUsuarioMutation.Field()
    update_usuario = UpdateUsuarioMutation.Field()
    delete_usuario = DeleteUsuarioMutation.Field()

    # register = mutations.Register.Field()
    verify_account = mutations.VerifyAccount.Field()
    token_auth = mutations.ObtainJSONWebToken.Field()
    set_password = mutations.PasswordSet.Field()
    change_passowrd = ChangePassword.Field()
    verify_token = mutations.VerifyToken.Field()
    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()

    # test = ObtainJSONWebTokenTest.Field()
