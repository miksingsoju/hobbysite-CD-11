from django.shortcuts import render, get_object_or_404
from .models import Article

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/article_list.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

#optional
# class ArticleListView(ListView):
#     model = Article
#     template_name = 'blog/article_list.html'
#     context_object_name = 'articles'

# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'blog/article_detail.html'
#     context_object_name = 'article'

