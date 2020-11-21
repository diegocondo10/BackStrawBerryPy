from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from apps.Auth.models import Aplicacion, Usuario, Permiso, Grupo


class AplicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aplicacion
        fields = ALL_FIELDS


class PermisoSerializer(serializers.ModelSerializer):
    aplicacion = AplicacionSerializer(read_only=True)
    aplicacion_id = serializers.PrimaryKeyRelatedField(
        queryset=Aplicacion.objects.all(),
        source='aplicacion',
        write_only=True,
        required=False
    )

    class Meta:
        model = Permiso
        fields = ALL_FIELDS
        extra_kwargs = {
            'aplicacion': {'required': False}
        }


class GrupoSerializer(serializers.ModelSerializer):
    permisos = PermisoSerializer(many=True, read_only=True)
    permisos_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permiso.objects.all(),
        source='permisos',
        write_only=True,
        required=False
    )

    class Meta:
        model = Grupo
        fields = ALL_FIELDS


class UsuarioSerializer(serializers.ModelSerializer):
    grupos = GrupoSerializer(many=True, read_only=True)
    grupos_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Grupo.objects.all(),
        source='grupos',
        write_only=True
    )
    permisos = PermisoSerializer(many=True, read_only=True)
    permisos_id = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Permiso.objects.all(),
        source='permisos',
        write_only=True
    )

    class Meta:
        model = Usuario
        fields = ALL_FIELDS
