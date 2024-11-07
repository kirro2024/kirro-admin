from django.contrib import admin

from .models import JobTracker


# Customising the admin interface
admin.site.site_header = 'Kirro Site Admin'
admin.site.site_title = 'Kirro Site Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'applicant', 'applicant_name', 'company_applied_to', 
        'position_applied', 'date_submitted', 'experience_required', 
        'resume_used', 'application_status', 'job_notes', 
        'created_by', 'updated_by',
        ]

