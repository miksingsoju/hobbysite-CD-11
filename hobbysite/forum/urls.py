from django.urls import path
from .views import thread_list, threads_by_category, thread_detail

urlpatterns = [
    path('threads', thread_list, name='thread_list'),
    path('threads/<int:category_id>', threads_by_category, name='threads_by_category'),
    path('thread/<int:thread_id>/', thread_detail, name='thread_detail'),
]

app_name = "forum"