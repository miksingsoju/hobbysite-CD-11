from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # author, created_on, updated_on are excluded
        fields = ['title', 'category', 'entry', 'header_image']
        widgets = {
            'entry': forms.Textarea(attrs={'rows': 6, 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'header_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # author, article, created_on, updated_on are excluded
        fields = ['entry']
        widgets = {
            'entry': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
