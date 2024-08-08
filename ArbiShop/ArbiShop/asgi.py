"""
ASGI config for ArbiShop project.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ArbiShop.settings')

application = get_asgi_application()
