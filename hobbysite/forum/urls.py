from django.urls import path
from .views import thread_list, thread_detail, thread_update, thread_create

urlpatterns = [
    path('threads', thread_list, name='thread_list'),
    path('thread/<int:thread_id>/', thread_detail, name='thread_detail'),
    path('thread/<int:thread_id>/edit', thread_update, name='thread_update'),
    path('thread/add', thread_create, name="thread_create")
]

app_name = "forum"