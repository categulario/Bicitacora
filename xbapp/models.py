# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth import get_user_model

class Ciclista(models.Model):
    """Define a un usuario del sistema"""
    nombre              = models.CharField(max_length=70, blank=True)
    facebook            = models.CharField(max_length=70, blank=True)
    twitter             = models.CharField(max_length=70, blank=True)
    score               = models.IntegerField(default=0)
    sexo                = models.CharField(max_length=1, choices=(
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ), default='M')
    fecha_nacimiento    = models.DateField(blank=True, null=True)
    fecha_registro      = models.DateField(auto_now_add=True)
    usuario             = models.ForeignKey(get_user_model())

    def __unicode__(self):
        return self.nombre

class Ruta(models.Model):
    """Una ruta recorrida y marcada por un usuario"""
    hora_inicio         = models.DateTimeField()
    hora_fin            = models.DateTimeField()
    ciclista            = models.ForeignKey(Ciclista)

class Punto(models.Model):
    """Define un punto de una ruta marcado por el GPS"""
    latitud             = models.FloatField()
    longitud            = models.FloatField()
    altitud             = models.IntegerField()
    ruta                = models.ForeignKey(Ruta)

class TipoLugar(models.Model):
    """Sirve para clasificar los lugares que encuentra el ciclista, como
    talleres o biciestacionamientos"""
    nombre              = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Lugar(models.Model):
    """Un punto importante para un ciclista, como un taller"""
    nombre              = models.CharField(max_length=70, blank=True)
    direccion           = models.CharField(max_length=140, blank=True)
    latitud             = models.FloatField()
    longitud            = models.FloatField()
    altitud             = models.IntegerField()
    tipo                = models.ForeignKey(TipoLugar)
    registrante         = models.ForeignKey(Ciclista)

    def __unicode__(self):
        return self.nombre

class TipoSuceso(models.Model):
    """ayuda a clasificar sucesos en la actividad vial del ciclista"""
    nombre              = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

class Suceso(models.Model):
    """Un suceso vial reportado por un ciclista o peatón con la aplicación"""
    ciclista            = models.ForeignKey(Ciclista)
    descripcion         = models.CharField(max_length=140)
    latitud             = models.FloatField()
    longitud            = models.FloatField()
    altitud             = models.IntegerField()
    tipo                = models.ForeignKey(TipoSuceso)
    hora                = models.DateTimeField()

    def __unicode__(self):
        return self.descripcion