from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path('', RedirectView.as_view(url='articles', permanent=False), name='blog-redirect'),
    path('articles', views.article_list, name='article_list'),
    path('article/<int:article_id>', views.article_detail, name='article_detail'),
]

app_name = "blog"