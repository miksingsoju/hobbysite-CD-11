from django import forms
from .models import Commission, Job, JobApplication

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = ['title', 'description', 'status']
    status = forms.ChoiceField(choices=Commission.status_choices)

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        exclude = ['commission']

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = []