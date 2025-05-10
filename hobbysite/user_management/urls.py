from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="update_profile")
]

app_name = "user_management"