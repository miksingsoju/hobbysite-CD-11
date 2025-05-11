# blog/forms.py
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # We only need to declare which fields to include; widgets go in the template
        fields = ['title', 'category', 'entry', 'header_image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['entry']
