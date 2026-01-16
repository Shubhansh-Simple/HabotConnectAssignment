# django
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''Override existing django user model for future use'''

    class Meta:
        db_table            = 'users_customuser'
        verbose_name        = 'Account'
        verbose_name_plural = 'Accounts'
