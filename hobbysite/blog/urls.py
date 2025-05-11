from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('articles/', views.article_list, name='article_list'),
    path('articles/add/', views.article_add, name='article_add'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('article/<int:article_id>/edit/', views.article_edit, name='article_edit'),
]
