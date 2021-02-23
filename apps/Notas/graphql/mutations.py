import graphene
from graphene_django_cud.mutations import DjangoCreateMutation, DjangoUpdateMutation

from apps.Notas.models import NotaAlumno, EvidenciaNotaAlumno


class InsertEvidenciaNotaAlumnoMutation(DjangoCreateMutation):
    class Meta:
        model = EvidenciaNotaAlumno
        field_types = {
            "nota": graphene.ID(),
        }


class CreateNotaMutation(DjangoCreateMutation):
    class Meta:
        model = NotaAlumno
        many_to_many_extras = {
            "evidencias": {
                "add": {"type": "CreateEvidenciaNotaAlumnoInput"},
                "remove": {"type": "ID"},
            }
        }

    @classmethod
    def before_save(cls, root, info, input, obj: NotaAlumno):
        evidencias_add = input.get('evidencias_add', None)

        if evidencias_add is not None:
            for item in input.evidencias_add:
                item['nota_id'] = obj.pk
        return super(DjangoCreateMutation, cls).before_save(root, info, input, obj)


class UpdateNotaMutation(DjangoUpdateMutation):
    class Meta:
        model = NotaAlumno
        many_to_many_extras = {
            "evidencias": {
                "add": {"type": "CreateEvidenciaNotaAlumnoInput"},
                "remove": {"type": "ID"},
            }
        }

    @classmethod
    def before_save(cls, root, info, input, id, obj: NotaAlumno):
        evidencias_add = input.get('evidencias_add', None)

        if evidencias_add is not None:
            for item in input.evidencias_add:
                item['nota_id'] = id

        return super(DjangoUpdateMutation, cls).before_save(root, info, input, id, obj)
