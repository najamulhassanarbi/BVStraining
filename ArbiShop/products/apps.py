"""
File: products/apps.py

Description:
    Configuration class for the Products app, defining app-specific settings
    such as the default primary key field type and the app's name.
"""

from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
