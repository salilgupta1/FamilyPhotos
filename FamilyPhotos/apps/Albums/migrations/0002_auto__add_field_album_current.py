# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Album.current'
        db.add_column(u'Albums_album', 'current',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Album.current'
        db.delete_column(u'Albums_album', 'current')


    models = {
        u'Albums.album': {
            'Meta': {'object_name': 'Album'},
            'albumUID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'awsObjectName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'current': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['Albums']