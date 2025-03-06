from django.db import models

# Create your models here.
class ProductType(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    #TODO: Product Types should be sorted by name in ascending order

class Product(models.Model):
    Name = models.CharField(max_length=255)
    ProductType = models.ForeignKey(ProductType,on_delete=models.SET_NULL)
    Description = models.TextField
    Price = models.DecimalField(decimal_places=2)
    #TODO: Products should be sorted by name in ascending order




