from django.contrib import admin

from .models import JobTracker
from preferences.models import UserProfile
from django.db.models import F, Count


# Customising the admin interface
admin.site.site_header = 'Kirro App Admin'
admin.site.site_title = 'Kirro App Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(admin.ModelAdmin):
    list_display = [
        'applicant', 'company_applied_to', 
        'position_applied', 'date_submitted', 'experience_required', 
        'resume_used', 'application_status', 'shared_email', 'sensitive_info', 
        'job_notes', 'job_description_link', 'created_by', 'updated_by',
        'full_job_description', 'short_job_description', 'user_location', 
        'employment_preference', 'job_location', 'job_level', 'linkedin_url', 
        'application_count'
        ]
    list_filter = ['applicant__email',]
    
    def application_count(self, obj):
        job_tracker = list(JobTracker.objects.values("applicant").annotate(Count('applicant')))
        return job_tracker
