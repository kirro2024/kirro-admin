from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationStatus(models.TextChoices):
    """ Model Choices."""
    IN_PROGRESS = "In Progress", _("In Progress")
    APPLIED = "Applied", _("Applied")
    REJECTED = "Rejected", _("Rejected")
    INTERVIEW = "Interview", _("Interview")

