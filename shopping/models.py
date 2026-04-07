from django.db import models

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    brand = models.CharField(max_length=100)
    
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField()
    in_stock = models.BooleanField(null=True, blank=True)

    category = models.CharField(max_length=100)

    image = models.ImageField(upload_to='products/', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
