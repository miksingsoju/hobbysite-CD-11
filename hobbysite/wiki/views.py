from django.shortcuts import render
from .models import Article, ArticleCategory
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch
# For debugging only
from django.http import HttpResponse

# Storing homepage here since I coded it, prevents the need for a homepage app
def homepage(request):
    return render(request, "homepage.html")

# Shows the full list of articles sorted by category, makes use of the related name to query articles under each category in advance
# Shows memes if the database is empty when this is called
def articles(request):
    user_articles = Article.objects.none()
    if request.user.is_authenticated:
        user_articles = Article.objects.filter(author=request.user.profile).order_by("-created_on")
        other_articles = Article.objects.exclude(author=request.user.profile)
    else:
        other_articles = Article.objects.all()

    # Prefetch only the filtered other_articles for each category
    categories = ArticleCategory.objects.prefetch_related(
        Prefetch("articles", queryset=other_articles.order_by("-created_on"))
    ).order_by("name")
    
    context = {
        "user_articles": user_articles,
        "categories": categories
    }
    
    return render(request, "article_list.html", context)

   

# Gives the full details of the article
def article_detail(request, num=1):
    article = Article.objects.get(pk=num)
    return render(request, "article_detail.html", {"article": article})

def add_article(request):
    return HttpResponse("Hehe still under construction")

def edit_article(request, num=1):
    return HttpResponse("Hehe still under construction")