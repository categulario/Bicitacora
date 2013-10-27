# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from xbapp.forms import LugarForm

def inicio(request):
    data = {}
    return render_to_response('xbapp/inicio.html', data, context_instance=RequestContext(request))

@require_POST
def login(request):
    """Procesa el login"""
    if not request.user.is_authenticated():
        username = request.POST.get('correo')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                messages.success(request, '¡Bienvenido!')
            else:
                messages.error(request, 'Lo sentimos, esta cuenta está desactivada')
        else:
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
def captura_lugar(request):
    data = {
        'formulario': LugarForm()
    }
    return render_to_response('xbapp/captura_lugar.html', data, RequestContext(request))

@login_required
def perfil(request):
    data = {

    }
    return render_to_response('xbapp/perfil.html', data, RequestContext(request))