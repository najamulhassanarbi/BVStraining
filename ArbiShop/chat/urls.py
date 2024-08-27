"""
URL routing for the chat application.

This module defines the URL patterns for the chat application, mapping URLs to views that handle
chat room interactions, including creating or retrieving chat rooms and accessing specific chat rooms.
"""

from django.urls import path
import chat.views as chat_views

urlpatterns = [
    path('<int:room_id>/', chat_views.ChatRoomView.as_view(), name='chat_room'),
    path('start/<int:seller_id>/', chat_views.CreateOrGetChatRoomView.as_view(), name='create_or_get_chat_room'),
]
