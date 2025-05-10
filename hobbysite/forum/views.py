from django.shortcuts import render
from .models import ThreadCategory, Thread

def thread_list(request):
    categories = ThreadCategory.objects.all()
    ctx = {'categories': categories,}
    return render(request, 'post_list.html', ctx)

def threads_by_category(request, category_id):    
    category = ThreadCategory.objects.filter(id=category_id).first()
    threads = Thread.objects.filter(category=category)
    ctx = {
        'category': category,
        'threads': threads,
        }
    return render(request, 'posts_by_category.html', ctx)

def thread_detail(request, thread_id):
    thread = Thread.objects.filter(id=thread_id).first()
    ctx = {'thread': thread}
    return render(request, 'post_detail.html', ctx)