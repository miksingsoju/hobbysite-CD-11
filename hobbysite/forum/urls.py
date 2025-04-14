from django.urls import path
from .views import post_list, post_detail

urlpatterns = [
    path('threads/', post_list, name='threads'),
    path('thread/<int:num>/', post_detail, name='thread'),
]

app_name = "forum"