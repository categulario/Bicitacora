# -*- coding:utf-8 -*-
from django.http import HttpResponse

def inicio(request):
    return HttpResponse('Hola, humano', content_type="text/plain")

def registro(request):
    return HttpResponse('yei!', content_type='text/plain')