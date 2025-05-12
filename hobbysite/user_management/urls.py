from django.urls import path
from . import views

urlpatterns = [
    path('', views.update_profile, name="update_profile"),
    path('dashboard/', views.dashboard, name='dashboard')

]

app_name = "user_management"