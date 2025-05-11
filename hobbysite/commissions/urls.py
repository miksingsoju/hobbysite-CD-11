from django.urls import path
from .views import commission_list, commission_detail, commission_add, commission_edit, job_apply, job_detail

# configured urls to be used
urlpatterns = [
    path('list/', commission_list, name='list'),
    path('detail/<int:num>/', commission_detail, name='detail'),
    path('add/', commission_add, name = 'add'),
    path('<int:num>/edit', commission_edit, name='edit'),
    path('job/<int:num>/', job_detail, name='job'),
]

app_name = "commissions"