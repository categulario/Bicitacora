# -*- coding:utf-8 -*-
from django.db.models.signals import post_save, pre_save
from xbapp.models import Ciclista

def incrementa_matricula(sender, **kwargs):
    """crea la siguiente matrícula para ser usada por un alumno"""
    if kwargs['created']:
        n = NumeroMatricula.objects.filter(anio=current_year())[:1][0]
        m = NumeroMatricula(anio=current_year(), numero=n.numero+settings.ECOLE_MATRICULA_INCREMENTO)
        m.save()

post_save.connect(incrementa_matricula, sender=Ciclista)
