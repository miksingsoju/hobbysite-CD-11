from django.urls import path
from . import views

# I made homepage tempate at the start, storing here for easy access
urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('articles/', views.articles, name ="article_index"),
    path('article/<int:num>/', views.article_detail, name="article_detail"),
    path('article/add/', views.add_article, name="add_article"),
    path('article/<int:num>/edit/', views.edit_article, name="edit_article")
]

app_name = "wiki"