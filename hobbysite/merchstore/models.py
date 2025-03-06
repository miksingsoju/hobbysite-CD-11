from django.db import models

# Create your models here.
class ProductType(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    class Meta:
        ordering = ['Name']

class Product(models.Model):
    Name = models.CharField(max_length=255)
    ProductType = models.ForeignKey(ProductType,on_delete=models.SET_NULL, null=True)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=50,decimal_places=2,null=True)
    class Meta:
        ordering = ['Name']




