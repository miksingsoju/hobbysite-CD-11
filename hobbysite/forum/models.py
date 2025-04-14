from django.db import models

class PostCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Post Category'
        verbose_name_plural = 'Post Categories'

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        PostCategory, 
        on_delete=models.SET_NULL, 
        null=True,
        related_name="posts"
    )
    
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
