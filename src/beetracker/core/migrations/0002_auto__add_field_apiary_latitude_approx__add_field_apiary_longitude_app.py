# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Apiary.latitude_approx'
        db.add_column(u'core_apiary', 'latitude_approx',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=30, decimal_places=20),
                      keep_default=False)

        # Adding field 'Apiary.longitude_approx'
        db.add_column(u'core_apiary', 'longitude_approx',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=30, decimal_places=20),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Apiary.latitude_approx'
        db.delete_column(u'core_apiary', 'latitude_approx')

        # Deleting field 'Apiary.longitude_approx'
        db.delete_column(u'core_apiary', 'longitude_approx')


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
            'latitude_approx': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '30', 'decimal_places': '20'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '20'}),
            'longitude_approx': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '30', 'decimal_places': '20'}),
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