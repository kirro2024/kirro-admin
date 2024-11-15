from django.contrib import admin

from .models import UserProfile


@admin.register(UserProfile)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 'created_at', 'updated_at', 'email', 'first_name',
        'last_name', 'phone_number', 'profile_picture_url', 'resume_url',
        'job_preferences', 'userlocation'
    ]