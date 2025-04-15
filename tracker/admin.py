from django.contrib import admin
from charfield_filters.admin import CharFieldFilterMixin
from .models import JobTracker, UserJobMetaData
from more_admin_filters import MultiSelectDropdownFilter


# Customising the admin interface
admin.site.site_header = 'Kirro App Admin'
admin.site.site_title = 'Kirro App Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(CharFieldFilterMixin, admin.ModelAdmin):
    list_display = [
        'applicant', 'no_of_jobs_applied', 'no_of_interviews_landed',
        'company_applied_to', 'position_applied',
        'date_submitted', 'experience_required', 'application_status',
        'job_notes', 'job_description_link', 'created_by', 'updated_by',
        'short_job_description', 'user_location',
        'employment_preference', 'job_location', 'job_level']
    list_filter = [('applicant__email', MultiSelectDropdownFilter)]
    readonly_fields = [
        'applicant_uuid', 'no_of_jobs_applied',
        'no_of_interviews_landed', 'created_by',
        ]
    charfield_filter_fields = ['company_applied_to', 'position_applied',
        'short_job_description',
        ]
    charfield_filter_type = 'autocomplete_select'
    search_fields = ['applicant__email']    # search box in admin
    autocomplete_fields = ['applicant']     # implement search on foreignkey
    search_help_text = 'Use the Search box to search for a user.'


    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)


@admin.register(UserJobMetaData)
class UserJobMetaDataAdmin(CharFieldFilterMixin, admin.ModelAdmin):
    list_display = [
        'user_email', 'preferences_complete', 'shared_email',
        'shared_email_password', 'resume_url',
        ]
    readonly_fields = ['user_email']
    charfield_filter_fields = ['user_email']
    charfield_filter_type = 'autocomplete_select'
    search_fields = ['user_email']

