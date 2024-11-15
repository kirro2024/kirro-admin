from django.db import models

from preferences.models import UserProfile
from django.conf import settings
from .callables import ApplicationStatus
from encrypted_model_fields.fields import EncryptedCharField


class JobTracker(models.Model):
    """ Model a job application."""
    applicant = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        to_field='email',
        help_text='Email of applicant',
        )
    applicant_name = models.CharField(
        max_length=200, 
        help_text='Fullname of applicant',
        )
    company_applied_to = models.CharField(max_length=255)
    position_applied = models.CharField(max_length=255)
    date_submitted = models.DateField(auto_now_add=True)
    experience_required = models.CharField(max_length=50)
    resume_used = models.FileField(upload_to="uploads/%Y/%m/%d/")
    application_status = models.CharField(
        max_length=12,
        choices = ApplicationStatus,
        default=ApplicationStatus.IN_PROGRESS,
        )
    shared_email = models.EmailField()
    sensitive_info = EncryptedCharField(max_length=100)
    job_notes = models.TextField(null=True, blank=True)
    job_description_link = models.URLField(
        max_length=255, 
        help_text='link to job description',
        )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        limit_choices_to={"is_staff": True},
        related_name='dep_create',
        to_field='email',
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
    #application_counter = models.PositiveIntegerField(editable=False, default=0)
    


    class Meta:
        verbose_name_plural = 'Job Tracker Information'
        ordering = ['-applicant']


    def __str__(self):
        """ Return a string representation of the model object."""
        return self.applicant.email

    



        
            



