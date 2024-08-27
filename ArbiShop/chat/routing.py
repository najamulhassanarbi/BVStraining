"""
URL routing for WebSocket connections in the chat application.

This module defines the URL patterns for WebSocket connections, specifically mapping
URLs to the SellerChatConsumer, which handles real-time chat functionality for sellers.
"""

from django.urls import  re_path
from chat.consumer import SellerChatConsumer
websocket_urlpatterns = [
    re_path(r'ws/(?P<room_id>\d+)/$', SellerChatConsumer.as_asgi()),
]