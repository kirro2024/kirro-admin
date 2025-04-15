from django.db import models
from preferences.models import UserProfile
from django.conf import settings
from .callables import ApplicationStatus, JobType, JobMode, JobLevelPreference
#from encrypted_model_fields.fields import EncryptedCharField


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
    no_of_jobs_applied = models.PositiveIntegerField(blank=True, null=True)
    no_of_interviews_landed = models.PositiveIntegerField(blank=True, null=True)
    company_applied_to = models.CharField(max_length=255, help_text='[required]')
    position_applied = models.CharField(max_length=255, help_text='[required]')
    date_submitted = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    experience_required = models.CharField(max_length=50, help_text='[required]')
    application_status = models.CharField(
        max_length=12,
        choices=ApplicationStatus,
        default=ApplicationStatus.APPLIED,
        help_text='[required]'
        )
    job_description_link = models.URLField(max_length=255, help_text='[required]')
    full_job_description = models.TextField(help_text='[required]')
    short_job_description = models.CharField(max_length=255, help_text='[required]')
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
    resume_used = models.URLField(blank=True, null=True)
    offer_letter = models.URLField(blank=True, null=True)


    class Meta:
        managed = True
        verbose_name_plural = 'Job Tracker Information'
        ordering = ['-date_submitted']


    def __str__(self):
        """ Return a string representation of the model object."""
        return self.applicant.email


class UserJobMetaData(models.Model):
    """Model a User meta data."""
    user_email = models.EmailField(blank=True, null=True)
    shared_email = models.EmailField(blank=True, null=True)
    shared_email_password = models.CharField(max_length=100, blank=True, null=True)
    resume_url = models.URLField(blank=True, null=True)
    preferences_complete = models.BooleanField(blank=True, null=True)


    class Meta:
        managed = True
        verbose_name = 'User Meta Data'
        verbose_name_plural = 'User Meta Data'


    def __str__(self):
        """Return a string representation of the model object."""
        return self.user_email







