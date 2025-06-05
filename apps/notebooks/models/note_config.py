from django.db import models

class NoteConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    config_json = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_config'