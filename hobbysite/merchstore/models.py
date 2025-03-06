from django.db import models
from django.urls import reverse

# Create your models here.
class ProductType(models.Model):
    Name = models.CharField(max_length=255)
    Description = models.TextField()

    class Meta:
        ordering = ['Name']
    
    def get_absolute_url(self):
        return reverse('merchstore:productType-detail', args=[self.id])
    
    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=255)
    ProductType = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL, 
        null=True)
    
    Description = models.TextField()
    Price = models.DecimalField(
        max_digits=50,
        decimal_places=2,
        null=True)
    
    class Meta:
        ordering = ['Name']
    
    def get_absolute_url(self):
        return reverse('merchstore:product-detail', args=[self.id])
    
    def __str__(self):
        return self.Name





