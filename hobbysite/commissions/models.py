from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Created the commission model with a title, description, people required, creation and update date
class Commission(models.Model):
    status_choices = [('Open', 'Open'), ('Full', 'Full'), ('Completed', 'Completed'), ('Discontinued', 'Discontinued'), ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=status_choices, default='Open')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('commissions:detail', args=[self.pk])

# Created the Job model with a commission foreign key, comment entry,creation and update date
class Job(models.Model):
    status_choices = [('Open', 'Open'), ('Full', 'Full'),]
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE, related_name='job')
    role = models.CharField(max_length=255)
    people_required = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=status_choices, default='Open')
    
    class Meta:
        ordering = ['status', '-people_required', 'role']

    def __str__(self):
        return f"{self.role} ({self.status})"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    def __str__(self):
        return self.user.username
        

class JobApplication(models.Model):
    status_choices = [ ('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Rejected', 'Rejected'), ]
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    applicant = models.ForeignKey(Profile, on_delete=models.CASCADE)  
    status = models.CharField(max_length=10, choices=status_choices, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['status', '-applied_on']

    def __str__(self):
        return f"{self.applicant.user} - {self.status}"
