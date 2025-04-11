from django.urls import path
from .views import apology

urlpatterns = [
    path('threads/', apology, name='threads'),
    path('thread/<int:num>/', apology, name='thread'),
]

app_name = "forum"