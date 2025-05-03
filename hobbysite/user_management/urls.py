from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="update_profile")
]