from django.db import models
from preferences.models import UserProfile
from django.conf import settings
from .callables import ApplicationStatus, JobType, JobMode, JobLevelPreference
from encrypted_model_fields.fields import EncryptedCharField



class JobTracker(models.Model):
    """ Model a job application."""
    applicant = models.ForeignKey(
        UserProfile,
        on_delete=models.CASCADE,
        to_field='email',
        help_text='[required]',
        )
    applicant_uuid = models.UUIDField(
        blank=True,
        null=True,
        help_text="Applicant's User ID."
        )
    company_applied_to = models.CharField(max_length=255, help_text='[required]')
    position_applied = models.CharField(max_length=255, help_text='[required]')
    date_submitted = models.DateField(auto_now_add=True)
    experience_required = models.CharField(max_length=50, help_text='[required]')
    #resume_used = models.FileField(upload_to="uploads/%Y/%m/%d/")
    application_status = models.CharField(
        max_length=12,
        choices=ApplicationStatus,
        default=ApplicationStatus.APPLIED,
        help_text='[required]'
        )
    shared_email = models.EmailField(blank=True, null=True)
    shared_email_password = EncryptedCharField(max_length=100, blank=True, null=True)
    job_description_link = models.URLField(max_length=255, help_text='[required]')
    full_job_description = models.TextField(help_text='[required]')
    short_job_description = models.CharField(max_length=50, help_text='[required]')
    job_notes = models.TextField(blank=True, null=True)
    user_location = models.CharField(max_length=255, blank=True, null=True)
    employment_preference = models.CharField(
        max_length=20,
        choices=JobType,
        default=JobType.FULL_TIME,
        help_text='[required]'
    )
    job_location = models.CharField(
        max_length=20,
        choices=JobMode,
        default=JobMode.ONSITE,
        help_text='[required]'
    )
    job_level = models.CharField(
        max_length=20,
        choices=JobLevelPreference,
        default=JobLevelPreference.ENTRY_LEVEL,
        help_text='[required]'
    )
    linkedin_url = models.URLField(max_length=255, blank=True, null=True)
    created_by = models.CharField(
        max_length=255,
        help_text='Email of staff initially responsible for this task.',
        )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={"is_staff": True},
        related_name = 'dep_update',
        to_field='email',
        help_text='[required]',
        )
    salary_range = models.CharField(max_length=50, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'Job Tracker Information'
        ordering = ['-date_submitted']


    def __str__(self):
        """ Return a string representation of the model object."""
        return self.applicant.email








