# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Document.ready'
        db.delete_column('documents_document', 'ready')

    def backwards(self, orm):
        # Adding field 'Document.ready'
        db.add_column('documents_document', 'ready',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'courses.course': {
            'Meta': {'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'documents': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Document']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'})
        },
        'documents.document': {
            'Meta': {'object_name': 'Document'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'done': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'pages': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['documents.Page']", 'symmetrical': 'False'}),
            'points': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['upvotes.VoteDocument']"}),
            'refer': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_course'", 'to': "orm['courses.Course']"}),
            'size': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'}),
            'words': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True'})
        },
        'documents.page': {
            'Meta': {'object_name': 'Page'},
            'filename': ('django.db.models.fields.CharField', [], {'default': "'blank'", 'max_length': '100'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mininame': ('django.db.models.fields.CharField', [], {'default': "'blank'", 'max_length': '100'}),
            'num': ('django.db.models.fields.IntegerField', [], {}),
            'threads': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['messages.Thread']", 'symmetrical': 'False'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        },
        'documents.pendingdocument': {
            'Meta': {'object_name': 'PendingDocument'},
            'doc': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['documents.Document']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'messages.message': {
            'Meta': {'object_name': 'Message'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'reference': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['messages.Message']", 'null': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'thread': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['messages.Thread']"})
        },
        'messages.thread': {
            'Meta': {'object_name': 'Thread'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'msgs': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'back_thread'", 'symmetrical': 'False', 'to': "orm['messages.Message']"}),
            'poster': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'referc': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tcourse'", 'null': 'True', 'to': "orm['courses.Course']"}),
            'referd': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tdoc'", 'null': 'True', 'to': "orm['documents.Document']"}),
            'referp': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'back_tpage'", 'null': 'True', 'to': "orm['documents.Page']"}),
            'subject': ('django.db.models.fields.TextField', [], {})
        },
        'upvotes.votedocument': {
            'Meta': {'object_name': 'VoteDocument'},
            'cat_exam': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_others': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_project': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_reference': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_solution': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_summary': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'cat_support': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'category': ('django.db.models.fields.CharField', [], {'default': "'O'", 'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'score': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['documents']