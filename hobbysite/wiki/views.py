from django.shortcuts import render
from .models import Article, ArticleCategory

# Storing homepage here since I coded it, prevents the need for a homepage app
def homepage(request):
    return render(request, "homepage.html")

def articles(request):
    categories = ArticleCategory.objects.prefetch_related("articles").order_by("name")
    return render(request, "article_list.html", {"categories": categories})

def article_detail(request, num=1):
    article = Article.objects.get(pk=num)
    return render(request, "article_detail.html", {"article": article})