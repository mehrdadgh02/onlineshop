from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class Register_User(models.Model):
    email = models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=50, null=False)
    confirm_password = models.CharField(max_length=50)
    full_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'


class Login_User(models.Model):
    email = models.EmailField(max_length=200, null=False)
    password = models.CharField(max_length=50, null=False)
