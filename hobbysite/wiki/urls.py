from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name="homepage"),
    path('articles', views.article, name ="article_index"),
    path('article/<int:num>', views.article_detail, name="article_detail")
]

app_name = "wiki"