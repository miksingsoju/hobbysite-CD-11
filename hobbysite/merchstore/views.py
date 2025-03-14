from django.shortcuts import render
from .models import Product, ProductType

# This loads the list of products
def product_list(request):
    products = Product.objects.all()
    productTypes = ProductType.objects.all()
    ctx = {
        'products': products,
        'productTypes': productTypes
    }
    return render(request,'product_list.html',ctx)

# This loads the product information
def product_detail(request,num=1):
    product = Product.objects.get(id=num)
    ctx = {
        'product': product
    }
    return render(request,'product.html',ctx)

