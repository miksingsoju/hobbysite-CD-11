from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone
from .models import ThreadCategory, Thread, Comment
from .forms import ThreadForm, CommentForm

# Standard display views

def thread_list(request):
    categories = ThreadCategory.objects.all()
    threads = Thread.objects.all()
    no_cat_threads = Thread.objects.filter(category=None)

    # condition for login-only displays
    user_threads = None
    other_threads = None
    if request.user.is_authenticated:
        user_threads = Thread.objects.filter(author=request.user)
        other_threads = Thread.objects.exclude(author=request.user)

    ctx = {
        'categories': categories,
        'threads': threads,
        'no_cat_threads': no_cat_threads,
        'user_threads': user_threads,
        'other_threads': other_threads,
    }
    return render(request, 'thread_list.html', ctx)

def thread_detail(request, thread_id):
    thread = Thread.objects.filter(id=thread_id).first()
    threads = Thread.objects.filter(category=thread.category)
    comments = thread.comments.all()

    # code to handle prev/next (neighbor) navigation per thread
    # index of thread in threads queryset not to be confused with id of thread objects!
    # tldr: threads sorted by name, not ids. so id cannot be used directly

    prev = 0
    nxt = 0

    onlyInCategory = False

    if len(threads) == 1:
        onlyInCategory = True
        prev, nxt = 0, 0
        
    if len(threads) > 1:
        for index, tr in enumerate(threads):
            if tr == thread:
                if index == len(threads) - 1:
                    prev = index - 1
                    nxt = 0
                elif index == 0:
                    prev = len(threads) - 1
                    nxt = 1
                else:
                    prev = index - 1
                    nxt = index + 1

        if threads[prev] == threads[nxt]:
            onlyInCategory = "pair"

    ctx = {
        'thread': thread,
        'comments': comments,
        'prev_thread': threads[prev],
        'next_thread': threads[nxt],
        'onlyInCategory' : onlyInCategory,
        }

    # condition for login-only displays
    if request.user.is_authenticated:
        form = CommentForm()
        ctx['form'] = form

    if(request.method == "POST"):
        form = CommentForm(request.POST)
        if form.is_valid():
            cm = Comment()
            cm.author = request.user
            cm.createdOn = timezone.now() # format of timezone.now() matches DateTimeField in models.
            cm.updatedOn = cm.createdOn # if it's new, it's the same.

            cm.thread = thread
            cm.entry = form.cleaned_data.get('entry')
            cm.save()
    
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

@login_required
def thread_update(request, thread_id):
    thread = Thread.objects.filter(id=thread_id).first()
    form = ThreadForm()

    if(request.method == "POST"):
        form = ThreadForm(request.POST, request.FILES)
        if form.is_valid():
            tr = thread
            tr.updatedOn = timezone.now()

            tr.title = form.cleaned_data.get('title')
            tr.entry = form.cleaned_data.get('entry')
            tr.category = form.cleaned_data.get('category')
            tr.image = form.cleaned_data.get('image')
            tr.save()

            response = redirect(f"/forum/thread/{thread_id}") 
            return response # redirect to associated recipe's detailed view.

    ctx = { 
        "thread" : thread,
        "form" : form,
    }

    return render(request, 'thread_edit.html', ctx)