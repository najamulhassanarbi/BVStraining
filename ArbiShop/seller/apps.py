"""
seller/apps.py

Defines the application configuration for the seller app.
"""

from django.apps import AppConfig


class SellerConfig(AppConfig):
    """Configuration class for the seller app."""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'seller'
