# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Album.awsS3Storage'
        db.alter_column(u'Albums_album', 'awsS3Storage', self.gf('django.db.models.fields.URLField')(max_length=400))

    def backwards(self, orm):

        # Changing field 'Album.awsS3Storage'
        db.alter_column(u'Albums_album', 'awsS3Storage', self.gf('django.db.models.fields.URLField')(max_length=200))

    models = {
        u'Albums.album': {
            'Meta': {'object_name': 'Album'},
            'albumUID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'awsS3Storage': ('django.db.models.fields.URLField', [], {'max_length': '400'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['Albums']