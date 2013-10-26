# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Ciclista'
        db.create_table(u'xbapp_ciclista', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal(u'xbapp', ['Ciclista'])


    def backwards(self, orm):
        # Deleting model 'Ciclista'
        db.delete_table(u'xbapp_ciclista')


    models = {
        u'xbapp.ciclista': {
            'Meta': {'object_name': 'Ciclista'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['xbapp']