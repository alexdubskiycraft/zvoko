from django.db import models
from django.utils import timezone
from django.conf import settings
from shop.models import Product

class Basket(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="baskets")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="users")    

class Order(models.Model):
    class PaymentMethod(models.TextChoices):
        INSHOP = "in_shop", "Оплатити в магазині"
        NP = "np", "Оплатити на відділенні Нової Пошти"
        COURIER = "courier", "Оплатити кур'єру" 

    firstname = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=100)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices, default=PaymentMethod.INSHOP)
    address = models.CharField(max_length=255)
    
class OrderProduct(models.Model):
    price = models.FloatField()
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING, related_name="order_products")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_products")


class Shop(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=100)
    priority = models.IntegerField()

    class Meta:
        ordering = ["-priority"]
        
    def __str__(self):
        return self.name
