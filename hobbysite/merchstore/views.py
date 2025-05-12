from django.shortcuts import render, redirect
from collections import defaultdict

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages


from .models import *
from .forms import *

# Create your views here.

def product_list(request):
    productTypes = ProductType.objects.all()

    if request.user.is_authenticated:
        products = Product.objects.exclude(owner=request.user.profile)
        user_products = Product.objects.filter(owner=request.user.profile)

    else:
        products = Product.objects.all()
        user_products = Product.objects.none()
        
    ctx = {
        'products':products,
        'productTypes':productTypes,
        'user_products' : user_products
    }
    return render(request,'product_list.html',ctx)

def product_detail(request, num=1):
    product = Product.objects.get(pk=num)
    images = ProductImage.objects.filter(product=product)

    # Check if the user is trying to purchase their own product
    if request.method == 'POST':
        # Ensure the user is authenticated before proceeding
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to make a purchase.")
            return redirect('login')  # Redirect to the login page if the user is not authenticated

        # Create a TransactionForm instance from the POST data
        form = TransactionForm(request.POST)

        if form.is_valid():
            # Get the quantity from the form
            quantity = form.cleaned_data['amount']  # Assuming 'amount' is the correct field name for quantity

            # Check if stock is sufficient
            if quantity > product.stock:
                messages.error(request, "Not enough stock available!")
                return redirect('merchstore:product_detail', num=product.id)  # Re-render the page with the error message
            else:
                # Proceed with the transaction
                transaction = form.save(commit=False)
                transaction.product = product
                transaction.buyer = request.user.profile  # Assuming user has a related Profile model
                transaction.status = Transaction.Status.TO_PAY  # Default status can be 'TO_PAY'
                transaction.save()

                # Update the product stock
                product.stock -= quantity
                product.save()

                # Success message and redirection to cart
                messages.success(request, f"Successfully bought {quantity} of {product.name}!")
                return redirect('merchstore:cart')  # Redirect to the cart after the purchase

        else:
            messages.error(request, "There was an error with the transaction form.")
    else:
        # If it's a GET request, just show the form
        form = TransactionForm()

    ctx = {
        'product': product,
        'images': images,
        'form': form
    }

    return render(request, 'product_detail.html', ctx)
@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user.profile  # set owner manually
            product.save()
            return redirect('merchstore:product_detail', product.id)
    else:
        form = ProductForm()

    return render(request, 'product_create.html', {'form': form})

@login_required
def product_update(request, num):
    product = Product.objects.get(id=num)

    if product.owner != request.user.profile:
        return HttpResponseForbidden("You are not allowed to edit this product.")

    if request.method == 'POST':
        if 'name' in request.POST:  # Product form submitted
            form = ProductForm(request.POST, request.FILES, instance=product)
            image_form = ProductImageForm()  # empty for re-render

            if form.is_valid():
                product = form.save(commit=False)
                product.owner = request.user.profile
                product.status = 'Out of Stock' if product.stock == 0 else 'Available'
                product.save()
                return redirect('merchstore:product_detail', num=product.id)

        else:  # Image form submitted
            form = ProductForm(instance=product)  # unchanged
            image_form = ProductImageForm(request.POST, request.FILES)
            if image_form.is_valid():
                image = image_form.save(commit=False)
                image.product = product
                image.save()
                return redirect('merchstore:product_update', num=product.id)
    else:
        form = ProductForm(instance=product)
        image_form = ProductImageForm()

    existing_images = ProductImage.objects.filter(product=product)

    ctx = {
        'form': form,
        'image_form': image_form,
        'existing_images': existing_images
    }

    return render(request, 'product_update.html', ctx)

def cart(request):
     # Get all transactions of the current user (excluding "on cart" or filter as needed)
    if not request.user.is_authenticated:
        return redirect('login')  # or handle unauthorized access

    transactions = Transaction.objects.filter(buyer=request.user.profile)

    grouped = defaultdict(list)
    for t in transactions:
        if t.product and t.product.owner:
            t.total_price = t.product.price * t.amount  # Add this property for use in template
            grouped[t.product.owner].append(t)

    ctx = {
        'grouped_transactions': grouped.items(),
    }
    return render(request, 'cart.html', ctx)

def transactions(request):
    if not request.user.is_authenticated:
        return redirect('login')  # or handle unauthorized access

    # Get all transactions of the current user (as seller)
    transactions = Transaction.objects.filter(product__owner=request.user.profile)

    # Group by buyer
    grouped = defaultdict(list)
    for t in transactions:
        if t.buyer:
            grouped[t.buyer].append(t)

    # Calculate the total price for each transaction
    for buyer, transactions in grouped.items():
        for transaction in transactions:
            transaction.total_price = transaction.product.price * transaction.amount  # Calculate total price

    ctx = {
        'grouped_transactions': grouped.items(),  # will be a list of (buyer, [transactions])
    }

    return render(request, 'transactions.html', ctx)


