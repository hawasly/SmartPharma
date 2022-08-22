from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100,unique=True)
    note = models.CharField(max_length=1000,blank=True)

    class Meta:
        ordering = ['name']