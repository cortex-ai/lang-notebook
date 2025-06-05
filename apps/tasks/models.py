from django.db import models


class AiTask(models.Model):
    id = models.BigIntegerField(primary_key=True)
    note_id = models.BigIntegerField()
    biztype = models.CharField(max_length=100)
    status = models.CharField(max_length=50)
    result = models.JSONField(blank=True, null=True)
    errormsg = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ai_task'
# Auto-generated file
