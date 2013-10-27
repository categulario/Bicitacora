# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from xbapp.forms import LugarForm, APILoginForm, CiclistaForm
from xbapp.models import existe_usuario
from django.contrib.auth import get_user_model

MODELO_USUARIO = get_user_model()

def inicio(request):
    data = {}
    return render_to_response('xbapp/inicio.html', data, context_instance=RequestContext(request))

@require_POST
def login(request):
    """Procesa el login"""
    if not request.user.is_authenticated():
        username = request.POST.get('correo')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, '¡Bienvenido!')
            else:
                messages.error(request, 'Lo sentimos, esta cuenta está desactivada')
        else:
            # buscamos el correo, si no existe, lo mandamos a registro
            if existe_usuario(email=request.POST.get('correo', '')):
                messages.error(request, 'contraseña incorrecta')
            else:
                # lo procedemos a inscribir
                formulario = APILoginForm(request.POST)
                if formulario.is_valid():
                    nuevo_usuario = MODELO_USUARIO(username=username, email=username)
                    nuevo_usuario.set_password(password)
                    nuevo_usuario.save()
                    user = auth.authenticate(username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'Te has registrado!!')
                    messages.info(request, 'Termina de llenar tu perfil')
                    return HttpResponseRedirect('/perfil')
                else:
                    messages.warning(request, 'datos de registro inválidos')
                    return HttpResponseRedirect('/')
            messages.error(request, 'Nadie registrado con ese correo, verifique por favor')
    else:
        messages.warning(request, 'Ya tienes una sesión')
    return HttpResponseRedirect('/')

@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, 'Nos vemos pronto')
    return HttpResponseRedirect('/')

@login_required
def captura(request):
    data = {
        'formulario': LugarForm()
    }
    return render_to_response('xbapp/captura_lugar.html', data, RequestContext(request))

@login_required
def perfil(request):
    data = {
        'formulario': CiclistaForm(instance=request.user.ciclista)
    }
    if request.method == 'POST':
        formulario = CiclistaForm(request.POST, instance=request.user.ciclista)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Datos actualizados!')
        else:
            messages.error(request, 'Alguno de los datos no es válido')
        data['formulario'] = formulario
    return render_to_response('xbapp/perfil.html', data, RequestContext(request))

@login_required
def proyecto(request):
    data = {

    }
    return render_to_response('xbapp/proyecto.html', data, RequestContext(request))
@login_required
def estadisticas(request):
    data = {

    }
    return render_to_response('xbapp/estadisticas.html', data, RequestContext(request))
@login_required
def contacto(request):
    data = {

    }
    return render_to_response('xbapp/contacto.html', data, RequestContext(request))