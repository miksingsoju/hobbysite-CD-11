from django import forms
from django.forms import Form, ModelForm, CheckboxSelectMultiple
from .models import ThreadCategory, Thread, Comment

class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['title', 'entry', 'category', 'image']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']