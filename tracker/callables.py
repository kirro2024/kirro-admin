from django.db import models
from django.utils.translation import gettext_lazy as _


class ApplicationStatus(models.TextChoices):
    """ Model Choices."""
    APPLIED = "applied", _("Applied")
    REJECTED = "rejected", _("Rejected")
    INTERVIEW = "interview", _("Interview")
    OFFER = "offer", _("Offer")


class JobType(models.TextChoices):
    """Model Choices for job type."""
    FULL_TIME = "Full time", _("Full time")
    PART_TIME = "Part time", _("Part time")
    CONTRACT = "Contract", _("Contract")
    INTERNSHIP = "Internship", _("Internship")


class JobMode(models.TextChoices):
    """Model choices for job mode."""
    ONSITE = "On-site", _("On-site")
    HYBRID = "Hybrid", _("Hybrid")
    REMOTE = "Remote", _("Remote")


class JobLevelPreference(models.TextChoices):
    """Model choices for job level."""
    ENTRY_LEVEL = "Entry-level", _("Entry-level")
    MID_LEVEL = "Mid-level", _("Mid-level")
    SENIOR_LEVEL = "Senior-level", _("Senior-level")
    LEADERSHIP = "Leadership", _("Leadership")


class Plan(models.TextChoices):
    """Model Subscription Plans."""
    SELECT = "SELECT PLAN", _("Select plan")
    BASIC = "BASIC PLAN", _("Basic")
    PREMIUM = "PREMIUM PLAN", _("Premium")
    PRO = "PRO PLAN", _("Pro")


