from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

# Each model represents a TABLE
# Each model attribute/field represents a row on the table.

class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()

    

