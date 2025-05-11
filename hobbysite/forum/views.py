from django.shortcuts import render
from .models import ThreadCategory, Thread

def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()
    ctx = {
        'categories': categories,
        'threads': threads,
    }
    return render(request, 'list_view.html', ctx)

def thread_detail(request, thread_id):
    thread = Thread.objects.filter(id=thread_id).first()
    comments = thread.comments.all()
    ctx = {
        'thread': thread,
        'comments': comments,
        }
    return render(request, 'thread_detail.html', ctx)