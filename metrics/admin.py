from django.contrib import admin
from .models import Metrics
from django.db.models import F, Count
from tracker.models import JobTracker


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'jobs_applied', 'num_of_interviews_landed', 'plan', 
        'num_of_hours_saved', 'total_jobs_available', 'total_limit_left',
        ]


    def num_of_hours_saved(self, obj):
        """Return the number of hours saved."""
        result = Metrics.objects.update(hours_saved=F('jobs_applied')*15/60)
        return int(result)


    def total_limit_left(self, obj):
        """Return the limit left for each user."""
        result = Metrics.objects.update(limit_left=F('total_jobs_available')-F('jobs_applied'))
        return result

