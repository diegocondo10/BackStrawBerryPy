from collections import namedtuple

import graphene
from graphene_django import DjangoObjectType

from Auth.models import Aplicacion, Permiso, Grupo, Usuario

Song = namedtuple('Song', ('title', 'artist'))


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

    class Meta:
        model = Grupo

    def resolve_permisos_disponibles(self: Grupo, info):
        return Permiso.objects.exclude(id__in=self.permisos.get_queryset().values_list('id'))


class UsuarioType(DjangoObjectType):
    class Meta:
        model = Usuario
