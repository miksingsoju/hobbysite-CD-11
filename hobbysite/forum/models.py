from django.db import models
from django.contrib.auth.models import User

class CommonInfo(models.Model):
    class Meta:
        abstract = True

    author = models.ForeignKey(
        User, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
class ThreadCategory(models.Model):
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Thread Categories'

    def __str__(self):
        return self.name   

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

class Thread(CommonInfo):
    class Meta:
        ordering = ['-created_on']

    category = models.ForeignKey(
        ThreadCategory, 
        on_delete=models.SET_NULL, 
        related_name="threads",
        null=True,
        blank=True,
        )
    image = models.ImageField(
        upload_to='templates/images/', 
        null=True,
        blank=True,
        )
    title = models.CharField(max_length=255)

class Comment(CommonInfo):
    class Meta:
        ordering = ['created_on']

    thread = models.ForeignKey(
        Thread, 
        on_delete=models.CASCADE, 
        related_name="comments",
        )
    