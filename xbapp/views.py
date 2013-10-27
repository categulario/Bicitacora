# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpResponseRedirect

def inicio(request):
    data = {}
    return render_to_response('xbapp/inicio.html', data, context_instance=RequestContext(request))

@require_POST
def login(request):
    return HttpResponseRedirect('/')