from django.urls import path
from .views import apology

urlpatterns = [
    path('', apology ,name="product_list"),
]

app_name = "forum"