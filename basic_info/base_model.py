from django.db import models
from django.core.exceptions import FieldDoesNotExist


class BaseModel(models.Model):
    """parent model"""

    create_time = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='createtime1')
    update_time = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name='createtime2')

    class Meta:
        abstract = True
