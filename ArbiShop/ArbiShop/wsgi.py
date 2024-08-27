"""file:wsgi.py
    This module provides WSGI application for DjangoTimeProject.
    WSGI config for ArbiShop project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArbiShop.settings')

application = get_wsgi_application()
