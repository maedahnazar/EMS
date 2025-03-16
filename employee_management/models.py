from django.contrib.auth.models import AbstractUser
from django.db import models

from .manager import EmployeeManager


class Department(models.Model):
    name = models.CharField(max_length=255)

class Employee(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='employees', null=True, blank=True)
    salary = models.CharField(max_length=25)
    date_of_joining = models.DateTimeField(auto_now_add=True)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = EmployeeManager()

    def _str_(self):
        return self.email