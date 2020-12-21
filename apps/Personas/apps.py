from django.apps import AppConfig


class PersonasConfig(AppConfig):
    name = 'apps.Personas'

    def ready(self):
        from apps.Personas.models import FuncionPersonal

        try:
            functiones_personal_default = [
                FuncionPersonal(nombre='DOCENTE', codigo='docente'),
                FuncionPersonal(nombre='SECRETARIA', codigo='secretaria'),
                FuncionPersonal(nombre='CHOFER', codigo='chofer'),
                FuncionPersonal(nombre='TERAPEUTA', codigo='terapeuta'),
            ]
            if functiones_personal_default.__len__() != FuncionPersonal.objects.count():
                FuncionPersonal.objects.bulk_create(functiones_personal_default)

        except Exception as e:
            pass
