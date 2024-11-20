from django.db import models
from preferences.models import UserProfile
from tracker.callables import Plan


class Metrics(models.Model):
    """Model a user's metrics."""
    id = models.BigAutoField(primary_key=True)
    email = models.ForeignKey(
        UserProfile, 
        on_delete=models.CASCADE, 
        to_field='email',
        db_column='email',
        )
    jobs_applied = models.SmallIntegerField(blank=True, null=True)
    num_of_interviews_landed = models.SmallIntegerField(blank=True, null=True)
    hours_saved = models.SmallIntegerField()
    plan = models.CharField(
        max_length=15,
        choices=Plan,
        default=Plan.SELECT,
    )
    total_jobs_available = models.SmallIntegerField()
    limit_left = models.SmallIntegerField()


    class Meta:
        managed = True
        db_table = 'metrics'
        verbose_name_plural = 'Metrics'

    
    def __str__(self):
        return self.email_id

