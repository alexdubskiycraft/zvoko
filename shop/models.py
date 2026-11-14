from django.db import models
from django.utils import timezone
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    priority = models.IntegerField()
    key = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to="cats/",
        verbose_name="Категорії",
        default=""
    )

    class Meta:
        ordering = ["-priority"]

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=255)
    image = models.ImageField(
        upload_to="products/",
        verbose_name="Продукти",
        default=""
    )
    priority = models.IntegerField()
    brand = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="products")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-priority"]
    
    def __str__(self):
        return self.name
    
        