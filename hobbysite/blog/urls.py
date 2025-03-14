from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = "blog"

urlpatterns = [
    path('articles/<int:category_id>', views.articles_by_category, name='articles_by_category'),
    path('articles', views.article_list, name='article_list'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
]
