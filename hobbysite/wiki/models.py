from django.db import models
from django.urls import reverse
from user_management.models import Profile

class ArticleCategory(models.Model):
    name = models.CharField(max_length=50, unique=True) # Set unique to prevent duplicate Categories
    description = models.TextField()
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null=True, # Allows me to migrate this without breaking my database or setting a default model
        related_name="articles"
    )
    category = models.ForeignKey(
        ArticleCategory,
        on_delete=models.SET_NULL,  # Set to NULL when the category is deleted
        null=True, # So django does not crash out when category is deleted
        related_name="articles"
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # Only set when created
    updated_on = models.DateTimeField(auto_now=True)  # Updates on last model update

    class Meta:
        ordering = ["-created_on"]  # Sort articles by creation date in descending order

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): # Prevents the need for hard-coded
        return reverse('wiki:article_detail', args=[str(self.id)])
    
class Comment(models.Model):
    author = models.ForeignKey(
        Profile,
        on_delete=models.SET_NULL,
        null = True,
        related_name="comment"
    )
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name="comment"
    )
    entry = models.TextField
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["created_on"]