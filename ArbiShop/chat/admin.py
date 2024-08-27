"""
Admin configuration for the ChatRoom and ChatMessage models.

This module registers the ChatRoom and ChatMessage models with the Django admin site,
allowing them to be managed through the admin interface.
"""

from django.contrib import admin
from chat.models import ChatRoom, ChatMessage

admin.site.register(ChatRoom)
admin.site.register(ChatMessage)
