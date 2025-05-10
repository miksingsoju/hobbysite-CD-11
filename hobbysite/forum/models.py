from django.db import models

class ThreadCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Thread Category'
        verbose_name_plural = 'Thread Categories'

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        ThreadCategory, 
        on_delete=models.SET_NULL, 
        null=True,
        blank=True,
        related_name="threads"
    )
    
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Thread'
        verbose_name_plural = 'Threads'