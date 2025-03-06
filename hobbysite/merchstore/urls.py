from django.urls import path
from .views import product_detail, product_list

urlpatterns = [
    path('',product_list,name="product_list"), #index page
    path('items',product_list,name="product_list"),
    path('item/<int:num>/',product_detail,name="product-detail")
]

app_name = "merchstore"