# -*- coding:utf-8 -*-
import os
from fabric.api import local, settings, abort, run, env
from fabric.contrib.console import confirm
from fabric.context_managers import cd, lcd, settings, hide
from fabric.decorators import task
import urllib
import urllib2
import json

APP_NAME = 'XBTrack'
USER = 'developingo'
HOST = 'developingo.webfactional.com'
VENV_DIR = "/home/%s/envs/EntornoBicitacora"%USER
DJANGO_APP_ROOT = os.path.join(VENV_DIR, APP_NAME)
GUNICORN_CONFIG = "%s/gconfig.py"%DJANGO_APP_ROOT
GUNICORN_PIDFILE = "%s/gunicorn.pid" % DJANGO_APP_ROOT
WSGI_MODULE = 'xbtrack.wsgi'
STATIC_ROOT = '/home/%s/webapps/bicitacorastatic/static'%USER

env.hosts = ['%s@%s' % (USER, HOST)]

@task
def lmigrate():
    """Corre las migraciones respectivas"""
    local('./dev_manage.py migrate')

@task
def schema():
    """Crea las migraciones"""
    local('./dev_manage.py schemamigration xbapp --auto')

def virtualenv(venv_dir):
    """
    Context manager that establishes a virtualenv to use.
    """
    return settings(venv=venv_dir)

def run_venv(command, **kwargs):
    """
    Runs a command in a virtualenv (which has been specified using
    the virtualenv context manager)
    """
    run("source %s/bin/activate" % env.venv + " && " + command, **kwargs)

@task
def reqs():
    """Instala las nuevas dependencias del paquete en el servidor remoto"""
    with virtualenv(VENV_DIR):
        with cd(DJANGO_APP_ROOT):
            run_venv("pip install -r requirements.txt")

@task
def pull():
    with cd(DJANGO_APP_ROOT):
        run("git pull")

@task
def server_start():
    """Inicia el servidor"""
    with cd(DJANGO_APP_ROOT):
        run("%(venv_dir)s/bin/gunicorn -c %(config_file)s %(wsgimodule)s:application"%{
            'venv_dir': VENV_DIR,
            'config_file': GUNICORN_CONFIG,
            'wsgimodule': WSGI_MODULE
        })

@task
def server_restart():
    """
    Restarts the webserver that is running the Django instance
    """
    try:
        run("kill -HUP $(cat %s)" % GUNICORN_PIDFILE)
    except:
        server_start()

@task
def server_stop():
    try:
        run("kill -HUP $(cat %s)" % GUNICORN_PIDFILE)
    except:
        print 'el servidor no está corriendo'

@task
def memory():
    """Monitorea la memoria usada"""
    run("ps -u %s -o pid,rss,command | awk '{print $0}{sum+=$2} END {print \"Total\", sum/1024, \"MB\"}'"%USER)

@task
def static():
    """Recolecta los archivos estáticos en remoto"""
    with virtualenv(VENV_DIR):
        with cd(DJANGO_APP_ROOT):
            run_venv("./manage.py collectstatic -v 0 --noinput --clear")
    run("chmod -R ugo+r %s" % STATIC_ROOT)

@task
def errors(n=10):
    with cd(DJANGO_APP_ROOT):
        run("tail -n %d error.log"%int(n))

@task
def access_api():
    with cd(DJANGO_APP_ROOT):
        run("cat access.log | grep api")

@task
def access(n=10):
    with cd(DJANGO_APP_ROOT):
        run("tail -n %d access.log"%int(n))

@task
def access(n=10):
    with cd(DJANGO_APP_ROOT):
        run("tail -n %d debug.log"%int(n))

@task
def syncdb():
    with virtualenv(VENV_DIR):
        with cd(DJANGO_APP_ROOT):
            run_venv("./manage.py syncdb --all")
            run_venv("./manage.py migrate --fake")

@task
def migrate():
    with virtualenv(VENV_DIR):
        with cd(DJANGO_APP_ROOT):
            run_venv("./manage.py migrate")

@task
def deploy():
    pull()
    reqs()
    migrate()
    static()
    server_restart()

@task
def tsapiruta():
    ruta = {
        "hora_inicio"   : "2012-12-31 09:08:33",
        "hora_fin"      : "2012-12-31 09:08:33",
        "puntos"        : [
            {
                "latitud"   : 21.8989,
                "longitud"  : 19.8989,
                "altitud"   : 1420,
            },
            {
                "latitud"   : 22.8989,
                "longitud"  : 19.8989,
                "altitud"   : 1420,
            },
            {
                "latitud"   : 23.8989,
                "longitud"  : 19.8989,
                "altitud"   : 1420,
            },
        ],
        "longitud"          : 12.3,
        "desplazamiento"    : 8.3
    }
    data = urllib.urlencode({
        'token': '133da770-3e97-11e3-82a5-701a0416ad73',
        'ruta': json.dumps(ruta)
    })
    res = urllib2.urlopen(
        'http://ab-dev:8000/api/w/ruta',
        data
    )
    print res.read()

@task
def tsapilugar():
    lugar = {
        "nombre"    : "YoloBicis",
        "direccion" : "2º priv. bis de josé mancisidor #157-b",
        "latitud"   : 93.2323,
        "longitud"  : 23.4343,
        "altitud"   : 1420,
        "tipo"      : "biciestacionamiento",  #puede ser también "taller" o "gasolinera"
    }
    data = urllib.urlencode({
        'token': '133da770-3e97-11e3-82a5-701a0416ad73',
        'lugar': json.dumps(lugar)
    })
    res = urllib2.urlopen(
        'http://ab-dev:8000/api/w/lugar',
        data
    )
    print res.read()

@task
def test():
    pass