from django.db import models


class Metrics(models.Model):
    id = models.BigAutoField(primary_key=True)
    email = models.TextField(blank=True, null=True)
    jobs_applied = models.SmallIntegerField(blank=True, null=True)
    num_of_interviews_landed = models.SmallIntegerField(blank=True, null=True)
    hours_saved = models.SmallIntegerField(blank=True, null=True)
    total_limits = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metrics'
        verbose_name_plural = 'Metrics'

