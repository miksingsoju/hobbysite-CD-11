from django.contrib import admin
from .models import Commission, Job, JobApplication

# added admin panels containing the model parameters
class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    search_fields = ('title','description', 'status', 'created_on', 'updated_on', 'author',)
    list_display =  ('title','description', 'status', 'created_on', 'updated_on', 'author',)

class JobAdmin(admin.ModelAdmin):
    model = Job
    search_fields = ('commission', 'role', 'people_required', 'status', )
    list_display =  ('commission', 'role', 'people_required', 'status', )

class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication
    search_fields = ('job', 'applicant', 'status', 'applied_on',)
    list_display =  ('job', 'applicant', 'status', 'applied_on',)


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)