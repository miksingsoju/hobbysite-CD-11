from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobApplicationForm, JobForm
from django.forms import modelformset_factory
from user_management.models import Profile


# this will be called when the url is commissions/list and will take the template from the commissions_list.html file
def commission_list(request):
    if request.user.is_authenticated:
        user_commissions = Commission.objects.filter(author=request.user).order_by('-created_on')
        applied_commissions = Commission.objects.filter(job__applications__applicant=request.user.profile).exclude(author=request.user).distinct().order_by('-created_on')
        
        other_commissions = Commission.objects.exclude(author=request.user).exclude(job__applications__applicant=request.user.profile).annotate(custom_order=models.Case(
            models.When(status='Open', then=0),
            models.When(status='Full', then=1),
            models.When(status='Completed', then=2),
            models.When(status='Discontinued', then=3),
            default=4,
            output_field=models.IntegerField()
        )).order_by('custom_order', '-created_on').distinct()
        
    else:
        user_commissions = applied_commissions= None
        other_commissions = Commission.objects.annotate(custom_order=models.Case(
            models.When(status='Open', then=0),
            models.When(status='Full', then=1),
            models.When(status='Completed', then=2),
            models.When(status='Discontinued', then=3),
            default=4,
            output_field=models.IntegerField()
        )).order_by('custom_order', '-created_on')

    context = { 'user_commissions': user_commissions, 'applied_commissions' : applied_commissions, 'commissions' : other_commissions}
    return render(request, 'commissions_list.html', context)

# this will be called when the url is commissions/details/number and will take the template from the commissions_details.html file
def commission_detail(request, num = 1):   
    commission = get_object_or_404(Commission, pk = num)
    jobs = commission.job.all()
    # Prepare job data with accepted count, open slots and booleans isfull and alreadyapplied
    job_data = []
    for job in jobs:
        accepted_count = job.applications.filter(status='Accepted').count()
        is_full = accepted_count >= job.people_required

        already_applied = False
        if request.user.is_authenticated:
            profile = request.user.profile
            already_applied = job.applications.filter(applicant=profile).exists()
        job_data.append({
            'job': job,
            'accepted_count': accepted_count,
            'open_slots': job.people_required - accepted_count,
            'is_full': is_full,
            'already_applied': already_applied,
        })

    # Handle forms for job application
    if request.method == 'POST' and request.user.is_authenticated:
        job_id = request.POST.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        accepted_count = job.applications.filter(status='Accepted').count()

        if accepted_count < job.people_required:
            profile = request.user.profile
            if not JobApplication.objects.filter(job=job, applicant=profile).exists():
                JobApplication.objects.create(job=job, applicant=profile)
        return redirect('commissions:detail' , num=num)

    context = { 'commission': commission, 'job_data': job_data,}   
    return render(request, 'commissions_detail.html', context)

@login_required
def commission_add(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            commission = form.save(commit=False)
            commission.author = request.user  
            commission.save()
            return redirect('commissions:list') 
    else:
        form = CommissionForm()
    return render(request, 'commissions_add.html', {'form': form})

@login_required
def commission_edit(request, num=1):
    commission = get_object_or_404(Commission, pk = num)
    if commission.author != request.user:
        return redirect('commissions:list')
    
    JobFormSet = modelformset_factory(Job, form=JobForm, extra=1, can_delete=True, max_num=10)

    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        form.fields['status'].disabled = True  # prevent manual editing
        formset = JobFormSet(request.POST, queryset=commission.job.all())

        if form.is_valid() and formset.is_valid():
            form.save()

            jobs = formset.save(commit=False)
            for job in jobs:
                job.commission = commission  # link job to current commission
                job.save()

            for obj in formset.deleted_objects:
                obj.delete()

            return redirect('commissions:list')
    else:
        form = CommissionForm(instance=commission)
        formset = JobFormSet(queryset=commission.job.all())

    return render(request, 'commissions_edit.html', {'form': form, 'formset': formset, 'commission': commission})

@login_required
def job_detail(request, num=1):
    job = get_object_or_404(Job, pk=num)
    commission = job.commission
    if commission.author != request.user:
        return redirect('commissions:list')

    if request.method == 'POST':
        app_id = request.POST.get('application_id')
        action = request.POST.get('action')
        application = get_object_or_404(JobApplication, pk=app_id, job=job)

        if action in ['Accepted', 'Rejected']:
            application.status = action
            application.save()

    applicants = job.applications.all().select_related('applicant__user')
    return render(request, 'job_applicants.html', {'job': job,'applicants': applicants,})