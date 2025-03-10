from django.db import models
from django.urls import reverse

# Create your models here.
class Commission(model.Models):
    title = models.CharField(max_length=50)
    description = models.TextField()
    people_required = models.PositiveIntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:commission-detail', args=[self.id])



class Comment(model.Models):
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='commissions')
    entry = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'Comment on {self.commission.title}'

