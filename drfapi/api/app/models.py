from django.db import models
from django.db.models.base import Model

# Create your models here.

class todos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()