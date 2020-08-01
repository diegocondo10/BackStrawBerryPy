import graphene
import graphene_django

from Auth.graphql.types import AplicacionType, PermisoType, GrupoType, UsuarioType
from Auth.models import Aplicacion, Permiso, Grupo, Usuario


class AuthQueries(graphene.ObjectType):
    aplicaciones = graphene_django.DjangoListField(AplicacionType)
    aplicacion = graphene.Field(AplicacionType, id=graphene.Int(required=True))
    permisos = graphene_django.DjangoListField(PermisoType)
    permiso = graphene.Field(PermisoType, id=graphene.Int(required=True))
    grupos = graphene_django.DjangoListField(GrupoType)
    grupo = graphene.Field(GrupoType, id=graphene.Int(required=True))
    usuarios = graphene_django.DjangoListField(UsuarioType)
    usuario = graphene.Field(UsuarioType, id=graphene.Int(required=True))

    def resolve_aplicacion(self, info, id):
        return Aplicacion.objects.filter(id=id).first()

    def resolve_permiso(self, info, id):
        return Permiso.objects.filter(id=id).first()

    def resolve_grupo(self, info, id):
        return Grupo.objects.filter(id=id).first()

    def resolve_usuario(self, info, id):
        return Usuario.objects.filter(id=id).first()
