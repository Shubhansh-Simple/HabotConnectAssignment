# django
from django.db import models


class DepartmentChoices(models.TextChoices):
    HR = "HR", "HR"
    ENGINEERING = "Engineering", "Engineering"
    SALES = "Sales", "Sales"


class RoleChoices(models.TextChoices):
    MANAGER = "Manager", "Manager"
    DEVELOPER = "Developer", "Developer"
    ANALYST = "Analyst", "Analyst"
