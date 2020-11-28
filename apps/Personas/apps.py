from django.apps import AppConfig


class PersonasConfig(AppConfig):
    name = 'apps.Personas'

    def ready(self):
        from apps.Personas.models import FuncionPersonal
        functiones_personal_default = [
            FuncionPersonal(nombre='DOCENTE'),
            FuncionPersonal(nombre='SECRETARIA'),
            FuncionPersonal(nombre='CHOFER'),
            FuncionPersonal(nombre='TERAPEUTA'),
        ]

        if functiones_personal_default.__len__() != FuncionPersonal.objects.count():
            FuncionPersonal.objects.bulk_create(functiones_personal_default)
