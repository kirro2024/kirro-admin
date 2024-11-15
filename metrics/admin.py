from django.contrib import admin
from .models import Metrics


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = [
        'email', 'jobs_applied', 'num_of_interviews_landed', 'hours_saved',
        'total_limits',
        ]
