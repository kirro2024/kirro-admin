from django.contrib import admin
from django.db.models import JSONField
from django_json_widget.widgets import JSONEditorWidget
from .models import UserProfile


@admin.register(UserProfile)
class PreferencesAdmin(admin.ModelAdmin):
    list_display = [
        'user_id', 'created_at', 'updated_at', 'email', 'first_name',
        'last_name', 'phone_number', 'profile_picture_url', 'resume_url',

    ]
    formfield_overrides = {
        JSONField: {'widget': JSONEditorWidget},
    }
    list_filter = ['email']
