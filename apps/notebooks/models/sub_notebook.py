from django.db import models
class SubNotebook(models.Model):
    id = models.BigIntegerField(primary_key=True)
    notebook_id = models.BigIntegerField()
    parent_id = models.BigIntegerField()
    title = models.CharField(max_length=100)
    is_leaf = models.BooleanField(blank=True, null=True)
    config_id = models.BigIntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    sort = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    path = models.TextField()

    class Meta:
        managed = False
        db_table = 'sub_notebook'
