from django.contrib import admin
# app/admin.py
from .models import Product, ProductType

class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    list_display = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ('name', 'description','price')


# registering the model and the admin is what tells
# Django that admin pages must be generated for the models specified
admin.site.register(ProductType, ProductTypeAdmin)
admin.site.register(Product, ProductAdmin)
