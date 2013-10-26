# -*- coding:utf-8 -*-
import os
from fabric.api import local, settings, abort, run, env
from fabric.contrib.console import confirm
from fabric.context_managers import cd, lcd, settings, hide
from fabric.decorators import task

@task
def lmigrate():
    """Corre las migraciones respectivas"""
    local('./dev_manage.py migrate')

@task
def schema():
    """Crea las migraciones"""
    local('./dev_manage.py schemamigration xbapp --auto')