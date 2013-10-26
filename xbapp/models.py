from django.db import models
from django.contrib.auth import get_user_model

class Ciclista(models.Model):
    """Define a un usuario del sistema"""
    nombre          = models.CharField(max_length=70)
    facebook        = models.CharField(max_length=70, blank=True)
    twitter         = models.CharField(max_length=70, blank=True)
    score           = models.IntegerField(default=0)

    def __unicode__(self):
        return self.nombre