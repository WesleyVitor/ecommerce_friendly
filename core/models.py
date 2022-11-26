from django.db import models



class Product(models.Model):
    price = models.FloatField()
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name
# Create your models here.
