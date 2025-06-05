from django.db import models

class Notebook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    user_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notebook'
# Auto-generated file
