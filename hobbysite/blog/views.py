from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, ArticleCategory
from .forms import ArticleForm, CommentForm

@login_required
def article_list(request):
    """
    List View: shows logged‐in user’s own articles first, then all others,
    grouped by category for the “all other” section.
    """
    user_profile = request.user.profile
    your_articles = Article.objects.filter(author=user_profile).order_by('-created_on')
    other_articles = Article.objects.exclude(author=user_profile).order_by('-created_on')

    # Build a dict mapping each category → list of other_articles in that category
    categories = ArticleCategory.objects.all().order_by('name')
    grouped_articles = {
        category: other_articles.filter(category=category)
        for category in categories
        if other_articles.filter(category=category).exists()
    }

    return render(request, 'blog/article_list.html', {
        'user_articles': your_articles,
        'grouped_articles': grouped_articles,
    })

def article_detail(request, article_id):
    """
    Detail View: displays article, header image, related links,
    comments, and comment form if logged in.
    """
    article = get_object_or_404(Article, pk=article_id)
    related_articles = (
        Article.objects
               .filter(author=article.author)
               .exclude(pk=article.pk)[:2]
    )

    comment_form = None
    if request.user.is_authenticated:
        if request.method == 'POST' and 'comment_submit' in request.POST:
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.author = request.user.profile
                comment.article = article
                comment.save()
                return redirect('blog:article_detail', article_id=article.pk)
        else:
            comment_form = CommentForm()

    return render(request, 'blog/article_detail.html', {
        'article': article,
        'related_articles': related_articles,
        'comments': article.comments.all(),
        'comment_form': comment_form,
    })

@login_required
def article_add(request):
    """
    Create View: uses ArticleForm to add a new article.
    """
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user.profile
            article.save()
            return redirect('blog:article_detail', article_id=article.pk)
    else:
        form = ArticleForm()

    return render(request, 'blog/article_form.html', {
        'form': form,
        'title': 'Add Article',
    })

@login_required
def article_edit(request, article_id):
    """
    Update View: lets the author edit their own article.
    """
    article = get_object_or_404(Article, pk=article_id, author=request.user.profile)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('blog:article_detail', article_id=article.pk)
    else:
        form = ArticleForm(instance=article)

    return render(request, 'blog/article_form.html', {
        'form': form,
        'title': 'Edit Article',
    })
