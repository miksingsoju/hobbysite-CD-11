from .models import Profile
from django import forms

class ProfileForm(forms.Form):
    profile = forms.ModelChoiceField(label='Profile', queryset=Profile.objects.all())
    display_name = forms.CharField(label='New display name', max_length=63)
    bio = forms.CharField('New bio', max_length=100)