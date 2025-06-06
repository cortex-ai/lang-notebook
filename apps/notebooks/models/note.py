from django.db import models

class Note(models.Model):
    id = models.BigIntegerField(primary_key=True)
    note_leaf_id = models.BigIntegerField()
    content_json = models.JSONField()
    embedding = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note'
# Auto-generated file
