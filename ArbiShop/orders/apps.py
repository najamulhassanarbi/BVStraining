"""
apps.py

This module defines the configuration for the Orders app within the Django project.
"""

from django.apps import AppConfig


class OrdersConfig(AppConfig):
    """
    Configuration class for the Orders app.

    Sets the default primary key field type and the name of the app.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'orders'
