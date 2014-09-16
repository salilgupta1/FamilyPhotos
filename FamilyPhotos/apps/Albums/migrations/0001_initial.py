# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Album'
        db.create_table(u'Albums_album', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('albumUID', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=300, null=True, blank=True)),
            ('awsObjectName', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('timestamp', self.gf('django.db.models.fields.DateField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'Albums', ['Album'])


    def backwards(self, orm):
        # Deleting model 'Album'
        db.delete_table(u'Albums_album')


    models = {
        u'Albums.album': {
            'Meta': {'object_name': 'Album'},
            'albumUID': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'awsObjectName': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        }
    }

    complete_apps = ['Albums']