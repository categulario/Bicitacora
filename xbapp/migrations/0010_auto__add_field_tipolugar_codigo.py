# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TipoLugar.codigo'
        db.add_column(u'xbapp_tipolugar', 'codigo',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TipoLugar.codigo'
        db.delete_column(u'xbapp_tipolugar', 'codigo')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'xbapp.ciclista': {
            'Meta': {'object_name': 'Ciclista'},
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sexo': ('django.db.models.fields.CharField', [], {'default': "'M'", 'max_length': '1'}),
            'token': ('django.db.models.fields.CharField', [], {'default': "'b3166448-3ec0-11e3-bdce-701a0416ad73'", 'unique': 'True', 'max_length': '36'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'usuario': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
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
            'desplazamiento': ('django.db.models.fields.FloatField', [], {}),
            'hora_fin': ('django.db.models.fields.DateTimeField', [], {}),
            'hora_inicio': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {})
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
            'codigo': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50'}),
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