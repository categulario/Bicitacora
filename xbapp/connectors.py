# -*- coding:utf-8 -*-
from django.db.models.signals import post_save, pre_save
from xbapp.models import Ciclista
from django.contrib.auth import get_user_model

MODELO_USUARIO = get_user_model()

def crea_perfil(sender, **kwargs):
    """crea la siguiente matrícula para ser usada por un alumno"""
    if kwargs['created']:
        usuario = kwargs['instance']
        nuevo_ciclista  = Ciclista(usuario=usuario)
        nuevo_ciclista.save()

post_save.connect(crea_perfil, sender=MODELO_USUARIO)
