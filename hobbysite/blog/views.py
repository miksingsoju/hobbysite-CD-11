from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleCategory

def article_list(request):
    categories = ArticleCategory.objects.all()  # Retrieve all categories
    return render(request, 'blog/article_list.html', {
        'categories': categories,
    })

def articles_by_category(request, category_id):
    category = get_object_or_404(ArticleCategory, id=category_id)
    articles = Article.objects.filter(category=category)
    return render(request, 'blog/articles_by_category.html', {
        'category': category,
        'articles': articles,
    })

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})
