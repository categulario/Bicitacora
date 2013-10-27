# -*- coding:utf-8 -*-
from django.contrib import admin
from xbapp.models import *

class CiclistaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'token']

admin.site.register(Ciclista, CiclistaAdmin)
admin.site.register(Ruta)
admin.site.register(Punto)
admin.site.register(TipoLugar)
admin.site.register(Lugar)
admin.site.register(TipoSuceso)
admin.site.register(Suceso)