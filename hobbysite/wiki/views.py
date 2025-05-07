from django.shortcuts import render
from .models import Article, ArticleCategory
# For debugging only
from django.http import HttpResponse

# Storing homepage here since I coded it, prevents the need for a homepage app
def homepage(request):
    return render(request, "homepage.html")

# Shows the full list of articles sorted by category, makes use of the related name to query articles under each category in advance
# Shows memes if the database is empty when this is called
def articles(request):
    categories = ArticleCategory.objects.prefetch_related("articles").order_by("name")
    return render(request, "article_list.html", {"categories": categories})

# Gives the full details of the article
def article_detail(request, num=1):
    article = Article.objects.get(pk=num)
    return render(request, "article_detail.html", {"article": article})

def add_article(request):
    return HttpResponse("Hehe still under construction")

def edit_article(request, num=1):
    return HttpResponse("Hehe still under construction")