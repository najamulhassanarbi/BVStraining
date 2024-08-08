"""file: asgi.py
    This module provides an ASGI web server for Django.
"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTimeProject.settings')

application = get_asgi_application()
