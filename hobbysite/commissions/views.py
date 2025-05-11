from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db import models
from .models import Commission, Job, JobApplication
from .forms import CommissionForm, JobApplicationForm, JobForm
from django.forms import modelformset_factory


# this will be called when the url is commissions/list and will take the template from the commissions_list.html file
def commission_list(request):
    if request.user.is_authenticated:
        commissions = Commission.objects.all().distinct().order_by(models.Case(
                models.When(author=request.user , then=0),
                models.When(job__applications__applicant=request.user.profile , then=1),
                models.When(status='Open', then=2),
                models.When(status='Full', then=3),
                models.When(status='Completed', then=4),
                models.When(status='Discontinued', then=5),
                default=4,
                output_field=models.IntegerField()
            ), '-created_on'
        )
    else:
        commissions = Commission.objects.all().order_by(models.Case(
                models.When(status='Open', then=0),
                models.When(status='Full', then=1),
                models.When(status='Completed', then=2),
                models.When(status='Discontinued', then=3),
                default=4,
                output_field=models.IntegerField()
            ), '-created_on'
        )


    context = { 'commissions': commissions,}

    return render(request, 'commissions_list.html', context)

# this will be called when the url is commissions/details/number and will take the template from the commissions_details.html file
def commission_detail(request, num = 1):   
    commission = get_object_or_404(Commission, pk = num)
    jobs = commission.job.all()
    # Prepare job data with accepted count and open status
    job_data = []
    for job in jobs:
        accepted_count = job.applications.filter(status='Accepted').count()
        is_full = accepted_count >= job.people_required
        job_data.append({
            'job': job,
            'accepted_count': accepted_count,
            'open_slots': job.people_required - accepted_count,
            'is_full': is_full
        })

    # Handle application POST
    if request.method == 'POST' and request.user.is_authenticated:
        job_id = request.POST.get('job_id')
        job = get_object_or_404(Job, id=job_id)
        accepted_count = job.applications.filter(status='Accepted').count()

        if accepted_count < job.people_required:
            profile = request.user.profile
            if not JobApplication.objects.filter(job=job, applicant=profile).exists():
                JobApplication.objects.create(job=job, applicant=profile)
        return redirect('detail', pk=num)

    context = {
        'commission': commission,
        'job_data': job_data,
    }   
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
def job_apply(request):
    return render(request)