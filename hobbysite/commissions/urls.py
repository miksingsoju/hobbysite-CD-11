from django.urls import path
from .views import commission_list, commission_detail

# configured urls to be used
urlpatterns = [
    path('list/', commission_list, name='list'),
    path('detail/<int:num>/', commission_detail, name='detail'),
]

app_name = "commissions"