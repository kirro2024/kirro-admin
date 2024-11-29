from django.db import models
from uuid import uuid4
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
        help_text='Email of applicant',
        )
    applicant_uuid = models.UUIDField(blank=True, null=True)
    company_applied_to = models.CharField(max_length=255)
    position_applied = models.CharField(max_length=255)
    date_submitted = models.DateField(auto_now_add=True)
    experience_required = models.CharField(max_length=50)
    resume_used = models.FileField(upload_to="uploads/%Y/%m/%d/")
    application_status = models.CharField(
        max_length=12,
        choices=ApplicationStatus,
        default=ApplicationStatus.APPLIED,
        )
    shared_email = models.EmailField()
    sensitive_info = EncryptedCharField(max_length=100)
    job_description_link = models.URLField(
        max_length=255, 
        help_text='link to job description',
        )
    full_job_description = models.TextField()
    short_job_description = models.CharField(max_length=50)
    job_notes = models.TextField(
        null=True, 
        blank=True,
        help_text='(optional)'
        )
    user_location = models.CharField(max_length=255)
    employment_preference = models.CharField(
        max_length=20,
        choices=JobType,
        default=JobType.FULL_TIME,
    )
    job_location = models.CharField(
        max_length=20,
        choices=JobMode,
        default=JobMode.ONSITE,
    )
    job_level = models.CharField(
        max_length=20,
        choices=JobLevelPreference,
        default=JobLevelPreference.ENTRY_LEVEL,
    )
    linkedin_url = models.URLField(
        max_length=255,
        help_text='Enter the Linkedin url of the applicant',
        )
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
        help_text='Email of staff that updated this task.',
        )
    salary_range = models.CharField(max_length=100)
    

    class Meta:
        verbose_name_plural = 'Job Tracker Information'
        ordering = ['-applicant']


    def __str__(self):
        """ Return a string representation of the model object."""
        return self.applicant.email



        
            



