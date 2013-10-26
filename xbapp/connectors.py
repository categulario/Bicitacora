# -*- coding:utf-8 -*-
from django.db.models.signals import post_save, pre_save
from xbapp.models import Ciclista

def crea_perfil(sender, **kwargs):
    """crea la siguiente matrícula para ser usada por un alumno"""
    if kwargs['created']:
        nuevo_ciclista  = Ciclista()

post_save.connect(crea_perfil, sender=Ciclista)
