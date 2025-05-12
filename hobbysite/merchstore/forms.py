from django import forms
from .models import Product, Transaction, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model  = Product
        exclude = ['owner'] 

class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'description']
        extra = 3
        can_delete = True

class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField(min_value=1, initial=1)
    class Meta:
        model = Transaction
        fields = ['amount']
