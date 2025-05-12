from django import forms
from .models import Article, Comment, WikiImage

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["entry"]
        
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'category', 'entry']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'entry': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
class WikiImageForm(forms.ModelForm):
    class Meta:
        model = WikiImage
        fields = ['image', 'description']