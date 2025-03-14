from django.shortcuts import render
from .models import Article, ArticleCategory

def article_list(request):
    categories = ArticleCategory.objects.all()
    return render(request, 'blog/article_list.html', {
        'categories': categories,
    })

def articles_by_category(request, category_id):
    # Use filter to get the category; .first() returns None if not found
    category = ArticleCategory.objects.filter(id=category_id).first()
    if not category:
        return render(request, 'blog/articles_by_category.html', {
            'error': "Category not found.",
            'articles': [],
            'category': None,
        })
    # Filter articles that belong to this category
    articles = Article.objects.filter(category=category)
    return render(request, 'blog/articles_by_category.html', {
        'category': category,
        'articles': articles,
    })

def article_detail(request, article_id):
    # Use filter to retrieve the article; .first() returns None if not found
    article = Article.objects.filter(id=article_id).first()
    if not article:
        return render(request, 'blog/article_detail.html', {
            'error': "Article not found.",
            'article': None,
        })
    return render(request, 'blog/article_detail.html', {'article': article})
