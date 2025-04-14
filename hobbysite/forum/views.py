from django.shortcuts import render
from .models import PostCategory, Post

def post_list(request):
    categories = PostCategory.objects.prefetch_related("posts").order_by("name")
    ctx = {'categories': categories,}
    return render(request, 'post_list.html', ctx)

def post_detail(request, post_id):
    post = Post.objects.filter(id=post_id).first()
    if post:
        ctx = {'post': post}
    else:
        ctx = {
            'error': "Post not found.",
            'post': None,
        }
    return render(request, 'post_detail.html', ctx)