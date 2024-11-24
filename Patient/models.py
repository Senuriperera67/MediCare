
from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    nic = models.CharField(max_length=20)
    problem = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
