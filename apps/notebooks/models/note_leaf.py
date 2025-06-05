from django.db import models

class NoteLeaf(models.Model):
    id = models.BigIntegerField(primary_key=True)
    sub_notebook_id = models.BigIntegerField()
    title = models.TextField()
    description = models.TextField(blank=True, null=True)
    sort = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_leaf'
# Auto-generated file
