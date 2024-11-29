from django.db import models


class Metrics(models.Model):
    """Model a user's metrics."""
    id = models.BigAutoField(auto_created=True,primary_key=True,)
    user_uuid = models.UUIDField(blank=True, null=True, unique=True,)
    jobs_applied = models.SmallIntegerField(blank=True, null=True)
    num_of_interviews_landed = models.SmallIntegerField(blank=True, null=True)
    hours_saved = models.SmallIntegerField(blank=True, null=True)
    total_jobs_available = models.SmallIntegerField(blank=True, null=True)
    limit_left = models.SmallIntegerField(blank=True, null=True)


    class Meta:
        managed = True
        db_table = 'metrics'
        verbose_name_plural = 'Metrics'
        ordering = ['id']


