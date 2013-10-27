# -*- coding:utf-8 -*-
from django.http import HttpResponse
from xbapp.forms import APIRegistroForm
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
import json

MODELO_USUARIO = get_user_model()

def inicio(request):
    return HttpResponse('Hola, humano', content_type="text/plain")

@csrf_exempt
@require_POST
def registro(request):
    formulario = APIRegistroForm(request.POST)
    if formulario.is_valid():
        nuevo_usuario = MODELO_USUARIO(email=request.POST.get('correo'), username=request.POST.get('correo'))
        nuevo_usuario.set_password(request.POST.get('password'))
        nuevo_usuario.save()

        ciclista = nuevo_usuario.ciclista
        ciclista.nombre = request.POST.get('nombre')
        ciclista.sexo = request.POST.get('sexo')
        ciclista.fecha_nacimiento = request.POST.get('fecha_nacimiento')

        ciclista.save()

        result = {
            'token': ciclista.token,
            'error': 0,
        }
    else:
        result = {
            'error': 1,
            'msg': formulario.errors
        }
    print request.POST
    return HttpResponse(json.dumps(result), content_type='text/plain')