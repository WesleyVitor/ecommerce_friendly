from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    price = models.FloatField()
    description = models.TextField(max_length=255)
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class ItemProduct(models.Model):
    product = models.OneToOneField(Product, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()

class ShoppingCart(models.Model):
    list_items = models.ManyToManyField(ItemProduct)
    paid = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)


class Buy(models.Model):
    shoppingCart = models.OneToOneField(ShoppingCart, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)



# Create your models here.
