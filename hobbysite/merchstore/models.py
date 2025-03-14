from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return reverse('merchstore:productType-detail', args=[self.id])
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    productType = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL, 
        null=True)

    imageURL = models.CharField(max_length=2000)

    description = models.TextField()
    price = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        null=True)
    
    class Meta:
        ordering = ['name']
    
    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.id])
    
    def __str__(self):
        return self.name





