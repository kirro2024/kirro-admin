from django.contrib import admin

from .models import JobTracker


# Customising the admin interface
admin.site.site_header = 'Kirro App Admin'
admin.site.site_title = 'Kirro App Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(admin.ModelAdmin):
    list_display = [
        'applicant', 'applicant_uuid', 'company_applied_to',
        'position_applied', 'date_submitted', 'experience_required',
        'application_status', 'shared_email', 'shared_email_password',
        'job_notes', 'job_description_link', 'created_by', 'updated_by',
        'full_job_description', 'short_job_description', 'user_location',
        'employment_preference', 'job_location', 'job_level', 'linkedin_url']
    list_filter = ['applicant__email',]
    readonly_fields = ['applicant_uuid', 'created_by']


    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

