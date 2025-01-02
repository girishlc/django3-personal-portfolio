from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    datefld = models.DateField()
    description = models.CharField(max_length=250)
    