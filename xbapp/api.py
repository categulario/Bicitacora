# -*- coding:utf-8 -*-
from django.http import HttpResponse
from xbapp.forms import APIRegistroForm
from xbapp.forms import APILoginForm
from xbapp.forms import valida_ruta
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.core.exceptions import ValidationError
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

@csrf_exempt
@require_POST
def login(request):
    formulario = APILoginForm(request.POST)
    if formulario.is_valid():
        user = auth.authenticate(username=request.POST.get('correo', ''), password=request.POST.get('password', ''))
        if user is not None:
            if user.is_active:
                result = {
                    'error': 0,
                    'token': user.ciclista.token
                }
            else:
                result = {
                    'error': 3,
                    'msg': 'user_bloqued'
                }
        else:
            result = {
                'error': 2,
                'msg': 'invalid_user'
            }
    else:
        result = {
            'error': 1,
            'msg': 'invalid_data'
        }
    return HttpResponse(json.dumps(result), content_type='text/plain')

@csrf_exempt
@require_POST
def registra_ruta(request):
    if 'token' in request.POST and 'ruta' in request.POST:
        try:
            usuario = MODELO_USUARIO.objects.get(ciclista__token=request.POST.get('token', ''))
            try:
                ruta_dict = json.loads(request.POST.get('ruta', '{}'))
            except ValueError:
                result = {
                    'error': 1,
                    'msg': 'formato_invalido_no_json'
                }
            else:
                try:
                    valida_ruta(ruta_dict)
                    # Si pasa la validación
                except ValidationError, ve:
                    print ve.args
                    result = {
                        'error': 1,
                        'msg': str(ve)
                    }
        except MODELO_USUARIO.DoesNotExist:
            result = {
                'error': 2,
                'msg': 'invalid_user'
            }
    else:
        result = {
            'error': 1,
            'msg': 'invalid_data'
        }
    return HttpResponse(json.dumps(result), content_type='text/plain')