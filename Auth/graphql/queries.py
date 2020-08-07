import graphene
import graphene_django

from Auth.graphql.types import AplicacionType, PermisoType, GrupoType, UsuarioType
from Auth.models import Aplicacion, Permiso, Grupo, Usuario


class AuthQueries(graphene.ObjectType):
    aplicaciones = graphene.List(AplicacionType)
    aplicacion = graphene.Field(AplicacionType, id=graphene.ID(required=True))

    permisos = graphene.List(PermisoType)
    permiso = graphene.Field(PermisoType, id=graphene.ID(required=True))

    grupos = graphene.List(GrupoType)
    grupo = graphene.Field(GrupoType, id=graphene.ID(required=True))

    usuarios = graphene_django.DjangoListField(UsuarioType)
    usuario = graphene.Field(UsuarioType, id=graphene.ID(required=True))

    def resolve_aplicaciones(self, info):
        return Aplicacion.objects.all().order_by("id")

    def resolve_aplicacion(self, info, id):
        return Aplicacion.objects.filter(id=id).first()

    def resolve_permiso(self, info, id):
        return Permiso.objects.filter(id=id).first()

    def resolve_permisos(self, info):
        return Permiso.objects.all().order_by('nombre')

    def resolve_grupo(self, info, id):
        return Grupo.objects.filter(id=id).first()

    def resolve_usuario(self, info, id):
        return Usuario.objects.filter(id=id).first()
