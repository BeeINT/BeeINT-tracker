# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Apiary'
        db.create_table(u'core_apiary', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=20)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=30, decimal_places=20)),
        ))
        db.send_create_signal(u'core', ['Apiary'])

        # Adding model 'HAPlacement'
        db.create_table(u'core_haplacement', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apiary', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placement', to=orm['core.Apiary'])),
            ('hive', self.gf('django.db.models.fields.related.ForeignKey')(related_name='placement', to=orm['core.Hive'])),
            ('start_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['HAPlacement'])

        # Adding model 'Hive'
        db.create_table(u'core_hive', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('identifier', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['Hive'])

        # Adding model 'MapInformation'
        db.create_table(u'core_mapinformation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('apiary', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Apiary'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('tag_key', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag_value', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('api_response', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'core', ['MapInformation'])

        # Adding model 'ActivityIndication'
        db.create_table(u'core_activityindication', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hive', self.gf('django.db.models.fields.related.ForeignKey')(related_name='activityindication', to=orm['core.Hive'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('index', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'core', ['ActivityIndication'])


    def backwards(self, orm):
        # Deleting model 'Apiary'
        db.delete_table(u'core_apiary')

        # Deleting model 'HAPlacement'
        db.delete_table(u'core_haplacement')

        # Deleting model 'Hive'
        db.delete_table(u'core_hive')

        # Deleting model 'MapInformation'
        db.delete_table(u'core_mapinformation')

        # Deleting model 'ActivityIndication'
        db.delete_table(u'core_activityindication')


    models = {
        u'core.activityindication': {
            'Meta': {'object_name': 'ActivityIndication'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hive': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'activityindication'", 'to': u"orm['core.Hive']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {})
        },
        u'core.apiary': {
            'Meta': {'object_name': 'Apiary'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '20'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.haplacement': {
            'Meta': {'object_name': 'HAPlacement'},
            'apiary': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placement'", 'to': u"orm['core.Apiary']"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'hive': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'placement'", 'to': u"orm['core.Hive']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'core.hive': {
            'Meta': {'object_name': 'Hive'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'core.mapinformation': {
            'Meta': {'object_name': 'MapInformation'},
            'api_response': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'apiary': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['core.Apiary']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['core']