# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Ciclista.facebook'
        db.add_column(u'xbapp_ciclista', 'facebook',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Ciclista.twitter'
        db.add_column(u'xbapp_ciclista', 'twitter',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=70, blank=True),
                      keep_default=False)

        # Adding field 'Ciclista.score'
        db.add_column(u'xbapp_ciclista', 'score',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Ciclista.facebook'
        db.delete_column(u'xbapp_ciclista', 'facebook')

        # Deleting field 'Ciclista.twitter'
        db.delete_column(u'xbapp_ciclista', 'twitter')

        # Deleting field 'Ciclista.score'
        db.delete_column(u'xbapp_ciclista', 'score')


    models = {
        u'xbapp.ciclista': {
            'Meta': {'object_name': 'Ciclista'},
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        }
    }

    complete_apps = ['xbapp']