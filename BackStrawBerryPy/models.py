from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_estado = models.CharField(max_length=10, default='A')

    class Meta:
        abstract = True
