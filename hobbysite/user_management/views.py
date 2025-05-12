from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .forms import ProfileForm
from .models import Profile

# for debugging only
from django.http import HttpResponse
from blog.models import Article
# from wiki.models import Article as WikiArticle
# from forum.models import Thread
# from merchstore.models import Transaction
# from commissions.models import Commission,

@login_required
def dashboard(request):
    p = request.user.profile
    return render(request, 'user_management/dashboard.html', {
      'blog_articles':          Article.objects.all().order_by('-created_on'),
    #   'wiki_articles':        WikiArticle.objects.all().order_by('-created_on'),
    #   'forum_threads':        Thread.objects.all().order_by('-created_on'),
    #   'products_bought':      Transaction.objects.all().order_by('-created_on'),
    #   'products_sold':        Transaction.objects.all().order_by('-created_on'),
    #   'commissions_created':  Commission.objects.all().order_by('-created_on'),
    #   'commissions_joined':   JobApplication.objects.all().order_by('-created_on'),
    })


@login_required
def update_profile(request):
    profile = request.user.profile 
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ProfileForm(instance=profile)
    return render(request, "update_profile.html", {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Profile for this user
            Profile.objects.create(
                user=user,
                display_name=user.username,  # default name, can be edited later
                email_address=user.email if user.email else f"{user.username}@example.com",
                bio="",
            )

            login(request, user)
            return redirect('/')  # or your actual profile/homepage
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})