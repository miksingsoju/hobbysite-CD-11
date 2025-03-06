from django.shortcuts import render
from django.template import loader
from .models import Product

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    ctx = {
        'products': products
    }
    return render(request,'product_list.html',ctx)

def product_detail(request,num=1):
    product = Product.objects.get(id=num)
    ctx = {
        'product': product
    }
    return render(request,'product.html',ctx)

