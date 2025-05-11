from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from .models import ThreadCategory, Thread
from .forms import ThreadForm

# Standard display views

def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()
    no_cat_threads = Thread.objects.filter(category=None)

    user_threads = None
    if request.user.is_authenticated:
        user_threads = Thread.objects.filter(author=request.user)

    ctx = {
        'categories': categories,
        'threads': threads,
        'no_cat_threads': no_cat_threads,
        'user_threads': user_threads,
    }
    return render(request, 'thread_list.html', ctx)

def thread_detail(request, thread_id):
    thread = Thread.objects.filter(id=thread_id).first()
    comments = thread.comments.all()
    ctx = {
        'thread': thread,
        'comments': comments,
        }
    return render(request, 'thread_detail.html', ctx)

# Add and/or modify content views; requires login

@login_required
def thread_create(request):
    form = ThreadForm()

    if(request.method == "POST"):
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            tr = Thread()
            tr.author = request.user
            tr.createdOn = timezone.now() # format of timezone.now() matches DateTimeField in models.
            tr.updatedOn = tr.createdOn # if it's new, it's the same.

            tr.title = form.cleaned_data.get('title')
            tr.entry = form.cleaned_data.get('entry')
            tr.category = form.cleaned_data.get('category')
            tr.image = form.cleaned_data.get('image')
            tr.save()

    ctx = { 
        "form" : form,
    }

    return render(request, 'thread_create.html', ctx)