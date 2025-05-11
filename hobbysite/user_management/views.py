from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
# for debugging only
from django.http import HttpResponse

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
