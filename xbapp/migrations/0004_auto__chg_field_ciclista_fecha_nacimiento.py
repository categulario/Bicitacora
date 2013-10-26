# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Ciclista.fecha_nacimiento'
        db.alter_column(u'xbapp_ciclista', 'fecha_nacimiento', self.gf('django.db.models.fields.DateField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Ciclista.fecha_nacimiento'
        raise RuntimeError("Cannot reverse this migration. 'Ciclista.fecha_nacimiento' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Ciclista.fecha_nacimiento'
        db.alter_column(u'xbapp_ciclista', 'fecha_nacimiento', self.gf('django.db.models.fields.DateField')())

    models = {
        u'xbapp.ciclista': {
            'Meta': {'object_name': 'Ciclista'},
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'})
        },
        u'xbapp.lugar': {
            'Meta': {'object_name': 'Lugar'},
            'altitud': ('django.db.models.fields.IntegerField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {}),
            'longitud': ('django.db.models.fields.FloatField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'registrante': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.Ciclista']"}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.TipoLugar']"})
        },
        u'xbapp.punto': {
            'Meta': {'object_name': 'Punto'},
            'altitud': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {}),
            'longitud': ('django.db.models.fields.FloatField', [], {}),
            'ruta': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.Ruta']"})
        },
        u'xbapp.ruta': {
            'Meta': {'object_name': 'Ruta'},
            'ciclista': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.Ciclista']"}),
            'hora_fin': ('django.db.models.fields.DateTimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'xbapp.suceso': {
            'Meta': {'object_name': 'Suceso'},
            'altitud': ('django.db.models.fields.IntegerField', [], {}),
            'ciclista': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.Ciclista']"}),
            'descripcion': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'hora': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {}),
            'longitud': ('django.db.models.fields.FloatField', [], {}),
            'tipo': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['xbapp.TipoSuceso']"})
        },
        u'xbapp.tipolugar': {
            'Meta': {'object_name': 'TipoLugar'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'xbapp.tiposuceso': {
            'Meta': {'object_name': 'TipoSuceso'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['xbapp']