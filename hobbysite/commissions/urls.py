from django.urls import path
from .views import commission_list, commission_detail

urlpatterns = [
    path('list/', commission_list.as_view(), name='list'),
    path('detail/<int:pk>/', commission_detail.as_view(), name='detail'),
]

app_name = "commissions"