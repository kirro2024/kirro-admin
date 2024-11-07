from django.db import models

from django.utils.translation import gettext_lazy as _
from users.models import CustomUser


class JobTracker(models.Model):
    """ Model a job application."""


    class ApplicationStatus(models.TextChoices):
        """ Model Choices."""


        IN_PROGRESS = "In Progress", _("In Progress")
        APPLIED = "Applied", _("Applied")
        REJECTED = "Rejected", _("Rejected")
        INTERVIEW = "Interview", _("Interview")

    # Model fields
    applicant = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        to_field='email',
        limit_choices_to={'is_staff': False},
        help_text='Email (ID) of applicant',
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
    job_notes = models.TextField()
    created_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={"is_staff": True},
        related_name='dep_create',
        to_field='email',
        help_text='Email of staff initially responsible for this task.',
        )
    updated_by = models.ForeignKey(
        CustomUser, 
        on_delete=models.CASCADE, 
        limit_choices_to={"is_staff": True},
        related_name = 'dep_update',
        to_field='email',
        help_text='Email of staff that updated this task.',
        )


    class Meta:
        verbose_name_plural = 'Job Tracker Information'
        ordering = ['-applicant']
    

    def __str__(self):
        """ Return a string representation of the model object."""
        return self.applicant_name

