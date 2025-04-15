from django.contrib import admin
from .models import Metrics, AllMetrics


@admin.register(Metrics)
class MetricsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_uuid', 'jobs_applied', 'num_of_interviews_landed', 
        'hours_saved', 'total_jobs_available', 'limit_left',
        ]

    readonly_fields = [
        'id', 'user_uuid', 'jobs_applied', 'num_of_interviews_landed', 
        'hours_saved', 'total_jobs_available', 'limit_left',
        ]


@admin.register(AllMetrics)
class AllMetricsAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'user_uuid', 'jobs_applied', 'num_of_interviews_landed', 'hours_saved',
        ]

    readonly_fields = [
        'id', 'user_uuid', 'jobs_applied', 'num_of_interviews_landed', 'hours_saved',
        ]

