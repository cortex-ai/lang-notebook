
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
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


class NoteConfig(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    config_json = models.JSONField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'note_config.py'


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


class UserAccount(models.Model):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=50, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    password_hash = models.TextField()
    account_level = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'
