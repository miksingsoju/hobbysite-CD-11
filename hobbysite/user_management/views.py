from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ProfileForm

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
        # Create the user first
        user_form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user
            user = user_form.save()
            
            # Create the profile linked to the user
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Log the user in
            login(request, user)
            return redirect('homepage')
    else:
        user_form = UserCreationForm()
        profile_form = ProfileForm()
    
    return render(request, 'registration/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })