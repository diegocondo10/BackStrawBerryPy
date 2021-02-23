from graphene_django_cud.mutations import DjangoCreateMutation

from apps.Notas.models import NotaAlumno


class CreateNotaMutation(DjangoCreateMutation):
    class Meta:
        model = NotaAlumno
