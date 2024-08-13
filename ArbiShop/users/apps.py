"""
File: users/apps.py

Description:
    This module defines the configuration for the 'users' Django application.
    The UsersConfig class specifies settings such as the default auto field type for models
    and the name of the application.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
