"""
File: admin.py

Description:
    This module customizes the Django admin interface for managing users. It defines
    a custom user admin interface that uses the CustomUser model, providing additional
    fields and filtering options tailored to the application's specific needs.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    """
    Customizes the Django admin interface for the CustomUser model, allowing
    administrators to manage user details, roles, and permissions effectively.
    """
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", "first_name", "last_name", "role", "is_active", "is_staff", "is_superuser", "date_joined")
    list_filter = ("role", "is_active", "is_staff", "is_superuser")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "avatar", "bio")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "role", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "first_name", "last_name", "avatar", "bio", "role",
                "is_active", "is_staff", "is_superuser", "groups", "user_permissions"
            )}
         ),
    )

    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)
    filter_horizontal = ("groups", "user_permissions")


admin.site.register(CustomUser, CustomUserAdmin)
