"""file:wsgi.py
    This module provides WSGI application for DjangoTimeProject.
"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoTimeProject.settings')

application = get_wsgi_application()
