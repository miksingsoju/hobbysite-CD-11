from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
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
      'blog_articles':        Article.objects.filter(author=p),
    #   'wiki_articles':        WikiArticle.objects.filter(author=p),
    #   'forum_threads':        Thread.objects.filter(author=p),
    #   'products_bought':      Transaction.objects.filter(buyer=p),
    #   'products_sold':        Transaction.objects.filter(product__owner=p),
    #   'commissions_created':  Commission.objects.filter(author=p),
    #   'commissions_joined':   JobApplication.objects.filter(applicant=p),
    })


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
