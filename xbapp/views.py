# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext

def inicio(request):
    data = {}
    return render_to_response('xbapp/inicio.html', data, context_instance=RequestContext(request))
