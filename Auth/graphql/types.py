from collections import namedtuple

import graphene
from graphene_django import DjangoObjectType

from Auth.models import Aplicacion, Permiso, Grupo, Usuario



class AplicacionType(DjangoObjectType):
    nombre = graphene.String(description='Nombre de la aplicacion')

    class Meta:
        model = Aplicacion


class PermisoType(DjangoObjectType):
    aplicacion_id = graphene.ID()

    class Meta:
        model = Permiso

    def resolve_aplicacion_id(self: Permiso, info):
        return self.aplicacion.id


class GrupoType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    numero_permisos = graphene.Int()

    class Meta:
        model = Grupo

    def resolve_permisos_disponibles(self: Grupo, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))

    def resolve_numero_permisos(self: Grupo, info):
        return self.permisos.get_queryset().count()


class UsuarioType(DjangoObjectType):
    permisos_disponibles = graphene.List(PermisoType)
    grupos_disponibles = graphene.List(GrupoType)
    numero_permisos = graphene.Int()
    numero_grupos = graphene.Int()

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
