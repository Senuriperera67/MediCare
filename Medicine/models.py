# models.py
from django.db import models

class Medicine(models.Model):
    
    name = models.CharField(max_length=100)
    description = models.TextField()
    mrp = models.FloatField()
    price = models.FloatField()
    quantity = models.IntegerField()
    mfg_date = models.DateField()
    expiry_date = models.DateField()

    def __str__(self):
        return self.name


# Create your models here.
