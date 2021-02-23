from django.db import models


class BaseModel(models.Model):
    ACTIVO = "A"
    ELIMINADO = "E"
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_estado = models.CharField(max_length=10, default='A')

    class Meta:
        abstract = True

    def __to_json__(self):
        obj_json = self.__dict__
        obj_json['created_at'] = self.created_at.isoformat()
        obj_json['updated_at'] = self.updated_at.isoformat()
        obj_json.pop('_state')
        return obj_json
