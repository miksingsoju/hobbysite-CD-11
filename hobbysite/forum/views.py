from django.shortcuts import render
from .models import PostCategory, Post

def post_list(request):
    categories = PostCategory.objects.all()
    ctx = {'categories': categories,}
    return render(request, 'post_list.html', ctx)

def posts_by_category(request, category_id):
    # Use filter to get the category; .first() returns None if not found
    category = PostCategory.objects.filter(id=category_id).first()

    posts = Post.objects.filter(category=category)
    return render(request, 'posts_by_category.html', {
        'category': category,
        'posts': posts,
    })

def post_detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    ctx = {'post': post}
    return render(request, 'post_detail.html', ctx)