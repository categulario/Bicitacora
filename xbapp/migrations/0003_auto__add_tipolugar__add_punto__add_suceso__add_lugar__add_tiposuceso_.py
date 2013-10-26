# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'TipoLugar'
        db.create_table(u'xbapp_tipolugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'xbapp', ['TipoLugar'])

        # Adding model 'Punto'
        db.create_table(u'xbapp_punto', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('latitud', self.gf('django.db.models.fields.FloatField')()),
            ('longitud', self.gf('django.db.models.fields.FloatField')()),
            ('altitud', self.gf('django.db.models.fields.IntegerField')()),
            ('ruta', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.Ruta'])),
        ))
        db.send_create_signal(u'xbapp', ['Punto'])

        # Adding model 'Suceso'
        db.create_table(u'xbapp_suceso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ciclista', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.Ciclista'])),
            ('descripcion', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('latitud', self.gf('django.db.models.fields.FloatField')()),
            ('longitud', self.gf('django.db.models.fields.FloatField')()),
            ('altitud', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.TipoSuceso'])),
            ('hora', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'xbapp', ['Suceso'])

        # Adding model 'Lugar'
        db.create_table(u'xbapp_lugar', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=70, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('latitud', self.gf('django.db.models.fields.FloatField')()),
            ('longitud', self.gf('django.db.models.fields.FloatField')()),
            ('altitud', self.gf('django.db.models.fields.IntegerField')()),
            ('tipo', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.TipoLugar'])),
            ('registrante', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.Ciclista'])),
        ))
        db.send_create_signal(u'xbapp', ['Lugar'])

        # Adding model 'TipoSuceso'
        db.create_table(u'xbapp_tiposuceso', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'xbapp', ['TipoSuceso'])

        # Adding model 'Ruta'
        db.create_table(u'xbapp_ruta', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hora_inicio', self.gf('django.db.models.fields.DateTimeField')()),
            ('hora_fin', self.gf('django.db.models.fields.DateTimeField')()),
            ('ciclista', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['xbapp.Ciclista'])),
        ))
        db.send_create_signal(u'xbapp', ['Ruta'])

        # Adding field 'Ciclista.sexo'
        db.add_column(u'xbapp_ciclista', 'sexo',
                      self.gf('django.db.models.fields.CharField')(default='M', max_length=1),
                      keep_default=False)

        # Adding field 'Ciclista.fecha_nacimiento'
        db.add_column(u'xbapp_ciclista', 'fecha_nacimiento',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 26, 0, 0)),
                      keep_default=False)

        # Adding field 'Ciclista.fecha_registro'
        db.add_column(u'xbapp_ciclista', 'fecha_registro',
                      self.gf('django.db.models.fields.DateField')(auto_now_add=True, default=datetime.datetime(2013, 10, 26, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'TipoLugar'
        db.delete_table(u'xbapp_tipolugar')

        # Deleting model 'Punto'
        db.delete_table(u'xbapp_punto')

        # Deleting model 'Suceso'
        db.delete_table(u'xbapp_suceso')

        # Deleting model 'Lugar'
        db.delete_table(u'xbapp_lugar')

        # Deleting model 'TipoSuceso'
        db.delete_table(u'xbapp_tiposuceso')

        # Deleting model 'Ruta'
        db.delete_table(u'xbapp_ruta')

        # Deleting field 'Ciclista.sexo'
        db.delete_column(u'xbapp_ciclista', 'sexo')

        # Deleting field 'Ciclista.fecha_nacimiento'
        db.delete_column(u'xbapp_ciclista', 'fecha_nacimiento')

        # Deleting field 'Ciclista.fecha_registro'
        db.delete_column(u'xbapp_ciclista', 'fecha_registro')


    models = {
        u'xbapp.ciclista': {
            'Meta': {'object_name': 'Ciclista'},
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'fecha_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'fecha_registro': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '70'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'sexo': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
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