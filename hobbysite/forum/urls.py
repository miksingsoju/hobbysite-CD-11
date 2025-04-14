from django.urls import path
from .views import post_list, posts_by_category, post_detail

urlpatterns = [
    path('threads', post_list, name='post_list'),
    path('threads/<int:category_id>', posts_by_category, name='posts_by_category'),
    path('thread/<int:post_id>/', post_detail, name='post_detail'),
]

app_name = "forum"