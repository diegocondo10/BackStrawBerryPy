from django.apps import AppConfig


class PersonasConfig(AppConfig):
    name = 'apps.Personas'

    def ready(self):
        from apps.Personas.models import FuncionPersonal

        try:
            functiones_personal_default = [
                dict(nombre='DOCENTE', codigo='docente'),
                dict(nombre='SECRETARIO/A', codigo='secretaria'),
                dict(nombre='CHOFER', codigo='chofer'),
                dict(nombre='TERAPEUTA', codigo='terapeuta'),
                dict(nombre='DIRECTOR/A', codigo='director'),
            ]
            if functiones_personal_default.__len__() != FuncionPersonal.objects.count():
                # FuncionPersonal.objects.bulk_create(functiones_personal_default)
                for funcion in functiones_personal_default:
                    FuncionPersonal.objects.get_or_create(
                        nombre=funcion.get('nombre'),
                        codigo=funcion.get('codigo')
                    )
                pass
        except Exception as e:
            pass
