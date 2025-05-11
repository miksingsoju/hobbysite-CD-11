from django.urls import path
from .views import thread_list, thread_detail

urlpatterns = [
    path('threads', thread_list, name='thread_list'),
    path('thread/<int:thread_id>/', thread_detail, name='thread_detail'),
]

app_name = "forum"