from django.contrib import admin

from .models import JobTracker


# Customising the admin interface
admin.site.site_header = 'Kirro App Admin'
admin.site.site_title = 'Kirro App Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'applicant', 'applicant_name', 'company_applied_to', 
        'position_applied', 'date_submitted', 'experience_required', 
        'resume_used', 'application_status', 'shared_email', 'sensitive_info', 
        'job_notes', 'job_description_link', 'created_by', 'updated_by',
        ]
    list_filter = [
        'applicant__email', 'applicant_name', 'created_by', 'updated_by',
        ]
    

