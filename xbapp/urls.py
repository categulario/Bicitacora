# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include

urlpatterns = patterns('xbapp.views',
    url(r'^$', 'inicio'),
)

urlpatterns += patterns('xbapp.api',
    url(r'^api$', 'inicio'),
    url(r'^api/registro$', 'registro'),
    url(r'^api/login$', 'login'),
    url(r'^api/w/ruta$', 'registra_ruta'),
    url(r'^api/w/lugar$', 'registra_lugar'),
)
