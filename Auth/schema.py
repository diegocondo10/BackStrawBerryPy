import graphene
from graphql_auth import mutations

from Auth.graphql.mutations import *


class AuthMutations(graphene.ObjectType):
    create_aplicacion = CreateAplicacionMutation.Field()
    update_aplicacion = UpdateAplicacionMutation.Field()
    delete_aplicacion = DeleteAplicacionMutation.Field()

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

    # token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    # verify_token = graphql_jwt.Verify.Field()
    # refresh_token = graphql_jwt.Refresh.Field()

    # test = ObtainJSONWebTokenTest.Field()
