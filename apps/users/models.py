from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class UserAccount(AbstractBaseUser):
    id = models.BigIntegerField(primary_key=True)
    email = models.CharField(unique=True, max_length=254)
    username = models.CharField(max_length=50, blank=True, null=True)
    source = models.IntegerField(blank=True, null=True)
    password_hash = models.TextField()
    account_level = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    # Add the required fields for user creation
    REQUIRED_FIELDS = ['username']  # Excluding password because it's handled by AbstractBaseUser
    USERNAME_FIELD = 'email'  # Make sure email is the unique identifier for authentication
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserAccountManager()

    class Meta:
        managed = False
        db_table = 'user_account'


#如果你打算让 Django 迁移并管理该模型的表，删除 managed = False，然后运行以下命令
#python manage.py makemigrations
#python manage.py migrate