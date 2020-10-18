from django.apps import AppConfig


class MatriculasConfig(AppConfig):
    name = 'Matriculas'

    def ready(self):
        import Matriculas.signals
