from django.shortcuts import render, redirect
from .models import Article, ArticleCategory, Comment
from .forms import ArticleForm, CommentForm
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
    
    return render(request, "wiki/article_list.html", context)

   

# Gives the full details of the article
def article_detail(request, num=1):
    article = Article.objects.get(pk=num)
    related_articles = list(Article.objects.filter(category=article.category).order_by("created_on")) # allows me to traverse them in order
    comments = Comment.objects.filter(article=article).order_by('-created_on')
    
    # Handle logic for comments
    form = None
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user.profile
                comment.save()
                return redirect('wiki:article_detail', num=num)
        else:
            form = CommentForm()
            
    previous = None
    next_article = None
    
    # Get index of the viewed article, then look for potential previous or next articles
    try:
        index = related_articles.index(article)
    except ValueError:
        index = -1
        
    previous = related_articles[index - 1] if index > 0 else None
    next_article = related_articles[index + 1] if index + 1 < len(related_articles) else None
    
    context = {
        "article": article,
        "comments": comments,
        "form": form,
        "previous": previous,
        "next_article": next_article
    }
    
    return render(request, "wiki/article_detail.html", context)

@login_required
def add_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect(article.get_absolute_url())
    else:
        form = ArticleForm()
    
    return render(request, 'wiki/article_add.html', {'form': form})

def edit_article(request, num=1):
    article = Article.objects.get(pk=num)
    
    # Makes it so only the author of the article can edit it
    if article.author != request.user.profile:
        return redirect("wiki:article_detail", num=num)
    
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect("wiki:article_detail", num=article.pk)
    else:
        form = ArticleForm(instance=article)
        
    return render(request, "wiki/article_edit.html", {"form": form, "article": article})