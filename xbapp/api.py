# -*- coding:utf-8 -*-
from django.http import HttpResponse
from xbapp.forms import APIRegistroForm
from xbapp.forms import APILoginForm
from xbapp.forms import valida_ruta, valida_lugar
from xbapp.models import Ruta, Ciclista, Punto, Lugar, TipoLugar
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.core.exceptions import ValidationError
from functools import wraps
import json

MODELO_USUARIO = get_user_model()

def requiere_login(vista):
    """forza una vista a recibir el valor indicado por post"""
    @wraps(vista)
    def wrapper(*args, **kwds):
        request = args[0]
        if request.user.is_authenticated():
            return vista(*args, **kwds)
        else:
            result = {
                'error': 2,
                'msg': 'invalid_user'
            }
            return HttpResponse(json.dumps(result), content_type='text/plain')
    return wrapper

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
    print request.POST['ruta']
    if 'token' in request.POST and 'ruta' in request.POST:
        try:
            ciclista = Ciclista.objects.get(token=request.POST.get('token', ''))
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
                    # Si pasa la validación, guardamos la ruta
                    nueva_ruta = Ruta(
                        hora_inicio     = ruta_dict['hora_inicio'],
                        hora_fin        = ruta_dict['hora_fin'],
                        ciclista        = ciclista,
                        longitud        = ruta_dict['longitud'],
                        desplazamiento  = ruta_dict['desplazamiento'],
                    )
                    nueva_ruta.save()
                    for punto in ruta_dict['puntos']:
                        nuevo_punto = Punto(
                            ruta        = nueva_ruta,
                            latitud     = punto['latitud'],
                            longitud    = punto['longitud'],
                            altitud     = punto['altitud'],
                        )
                        nuevo_punto.save()
                    result = {
                        'error': 0,
                        'msg': 'ok'
                    }
                except ValidationError, ve:
                    result = {
                        'error': 1,
                        'msg': str(ve)
                    }
        except Ciclista.DoesNotExist:
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
def registra_lugar(request):
    if 'token' in request.POST and 'lugar' in request.POST:
        try:
            ciclista = Ciclista.objects.get(token=request.POST.get('token', ''))
            try:
                lugar_dict = json.loads(request.POST.get('lugar', '{}'))
            except ValueError:
                result = {
                    'error': 1,
                    'msg': 'formato_invalido_no_json'
                }
            else:
                try:
                    valida_lugar(lugar_dict)
                    # Si pasa la validación, guardamos la lugar
                    nuevo_lugar = Lugar(
                            nombre    = lugar_dict['nombre'],
                            direccion = lugar_dict['direccion'],
                            latitud   = lugar_dict['latitud'],
                            longitud  = lugar_dict['longitud'],
                            altitud   = lugar_dict['altitud'],
                            tipo      = TipoLugar.objects.get_or_create(codigo=lugar_dict['tipo'])[0],
                            registrante = ciclista
                    )
                    nuevo_lugar.save()
                    result = {
                        'error': 0,
                        'msg': 'ok'
                    }
                except ValidationError, ve:
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

@require_GET
@requiere_login
def obtener_token(request):
    result = {
        'token': request.user.ciclista.token,
        'error': 0
    }
    return HttpResponse(json.dumps(result), content_type='text/plain')