# Create your views here.
from rest_framework.viewsets import ModelViewSet

from Auth.models import Aplicacion, Permiso, Grupo, Usuario
from Auth.serializers import AplicacionSerializer, PermisoSerializer, GrupoSerializer, UsuarioSerializer


class AplicacionViewSet(ModelViewSet):
    queryset = Aplicacion.objects.all()
    serializer_class = AplicacionSerializer
    filterset_fields = {
        'nombre': ['icontains']
    }


class PermisoViewSet(ModelViewSet):
    queryset = Permiso.objects.all()
    serializer_class = PermisoSerializer
    filterset_fields = {
        'nombre': ['icontains'],
        'aplicacion__nombre': ['icontains']
    }
    ordering_fields = ['nombre', 'aplicacion__nombre']
    ordering = ['nombre', 'aplicacion__nombre']


class GrupoViewSet(ModelViewSet):
    queryset = Grupo.objects.all()
    serializer_class = GrupoSerializer
    filterset_fields = {
        'nombre': ['icontains']
    }
    ordering_fields = ['nombre', '-nombre']
    ordering = ['nombre', ]


class UsuarioViewset(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filterset_fields = {
        'username': ['icontains', 'exact']
    }
    ordering_fields = ['username']
    ordering = ['username', ]
