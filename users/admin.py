from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", 'first_name', 'last_name', "is_staff",)
    list_filter = ("email", 'first_name', 'last_name', "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", 'first_name', 'last_name', 'password1', 'password2', "is_staff",
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("id",)


admin.site.register(CustomUser, CustomUserAdmin)