""" File: main/apps.py
This module defines the configuration for the 'main' Django application.

The MainConfig class specifies settings such as the default auto field type for models
and the name of the application.
"""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Configuration class for the 'main' application."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
