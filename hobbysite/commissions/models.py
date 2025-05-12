from django.db import models
from django.urls import reverse

# Created the commission model with a title, description, people required, creation and update date
class Commission(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Meta class is for ordering based on 'created_on'
    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:detail', args=[self.pk])

# Created the Comment model with a commission foreign key, comment entry,creation and update date
class Comment(models.Model):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='comments')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    # Meta class is for ordering based on '-created_on' which means it will get the latest comment
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment on {self.commission.title}'