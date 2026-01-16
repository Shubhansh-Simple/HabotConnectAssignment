# django
from django.db import models

# local
from .utils.choices import DepartmentChoices, RoleChoices


class Employee(models.Model):
    '''Employee table to store company's employee information'''

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.CharField(
        max_length=50,
        choices=DepartmentChoices.choices,
        null=True,
        blank=True,
    )
    role = models.CharField(
        max_length=50,
        choices=RoleChoices.choices,
        null=True,
        blank=True,
    )
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Employee - {self.email}'
