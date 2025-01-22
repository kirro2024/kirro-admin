from django.contrib import admin
from charfield_filters.admin import CharFieldFilterMixin
from .models import JobTracker
from more_admin_filters import MultiSelectDropdownFilter


# Customising the admin interface
admin.site.site_header = 'Kirro App Admin'
admin.site.site_title = 'Kirro App Admin Portal'
admin.site.index_title = 'Welcome to Kirro Admin Portal'


@admin.register(JobTracker)
class JobTrackerAdmin(CharFieldFilterMixin, admin.ModelAdmin):
    list_display = [
        'applicant', 'company_applied_to', 'position_applied',
        'date_submitted', 'experience_required', 'application_status',
        'shared_email', 'resume_url', 'job_notes', 'job_description_link',
        'created_by', 'updated_by', 'short_job_description', 'user_location',
        'employment_preference', 'job_location', 'job_level']
    list_filter = [('applicant__email', MultiSelectDropdownFilter)]
    readonly_fields = ['applicant_uuid', 'created_by']
    charfield_filter_fields = ['company_applied_to', 'position_applied', 'short_job_description']
    charfield_filter_type = 'autocomplete_select'


    def save_model(self, request, obj, form, change):
        if not obj.created_by:
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

