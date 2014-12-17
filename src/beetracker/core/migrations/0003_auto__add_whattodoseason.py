# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'WhatToDoSeason'
        db.create_table('core_whattodoseason', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kw_start', self.gf('django.db.models.fields.IntegerField')()),
            ('kw_end', self.gf('django.db.models.fields.IntegerField')()),
            ('headline', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('headline_de', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('headline_en', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('copy', self.gf('django.db.models.fields.TextField')(max_length=255)),
            ('copy_de', self.gf('django.db.models.fields.TextField')(blank=True, max_length=255, null=True)),
            ('copy_en', self.gf('django.db.models.fields.TextField')(blank=True, max_length=255, null=True)),
        ))
        db.send_create_signal('core', ['WhatToDoSeason'])


    def backwards(self, orm):
        # Deleting model 'WhatToDoSeason'
        db.delete_table('core_whattodoseason')


    models = {
        'core.activityindication': {
            'Meta': {'object_name': 'ActivityIndication'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'hive': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Hive']", 'related_name': "'activityindication'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'index': ('django.db.models.fields.IntegerField', [], {})
        },
        'core.apiary': {
            'Meta': {'object_name': 'Apiary'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '20'}),
            'latitude_approx': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '30', 'decimal_places': '20'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '20'}),
            'longitude_approx': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '30', 'decimal_places': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.haplacement': {
            'Meta': {'object_name': 'HAPlacement'},
            'apiary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Apiary']", 'related_name': "'placement'"}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'hive': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Hive']", 'related_name': "'placement'"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'})
        },
        'core.hive': {
            'Meta': {'object_name': 'Hive'},
            'comment': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'identifier': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.mapinformation': {
            'Meta': {'object_name': 'MapInformation'},
            'api_response': ('django.db.models.fields.TextField', [], {'blank': 'True', 'null': 'True'}),
            'apiary': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Apiary']"}),
            'date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tag_key': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_value': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.whattodoseason': {
            'Meta': {'object_name': 'WhatToDoSeason'},
            'copy': ('django.db.models.fields.TextField', [], {'max_length': '255'}),
            'copy_de': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'copy_en': ('django.db.models.fields.TextField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'headline': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headline_de': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'headline_en': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kw_end': ('django.db.models.fields.IntegerField', [], {}),
            'kw_start': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['core']