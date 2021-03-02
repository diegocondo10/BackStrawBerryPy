import graphene
from graphene_django import DjangoObjectType

from apps.Auth.models import Permiso, Grupo, Usuario
from utils.functions import validate_can_delete


class PermisoType(DjangoObjectType):
    class Meta:
        model = Permiso


class GrupoType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    numero_permisos = graphene.Int()
    can_delete = graphene.Boolean()

    class Meta:
        model = Grupo

    def resolve_permisos_disponibles(self: Grupo, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))

    def resolve_numero_permisos(self: Grupo, info):
        return self.permisos.get_queryset().count()

    def resolve_can_delete(self: Grupo, info):
        return validate_can_delete(self.usuario_set.count())


class UsuarioType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    grupos_disponibles = graphene.List(GrupoType)
    numero_permisos = graphene.Int()
    numero_grupos = graphene.Int()
    can_delete = graphene.Boolean()

    class Meta:
        model = Usuario

    def resolve_permisos_disponibles(self: Usuario, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))

    def resolve_grupos_disponibles(self: Usuario, info):
        return Grupo.objects.exclude(id__in=self.grupos.get_queryset().values_list('id'))

    def resolve_numero_permisos(self: Usuario, info):
        return self.permisos.get_queryset().count()

    def resolve_numero_grupos(self: Usuario, info):
        return self.grupos.get_queryset().count()

    def resolve_can_delete(self: Usuario, info):
        return self.persona_id is None
