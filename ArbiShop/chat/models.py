"""
Models for chat rooms and messages in a Django application.

This file defines the ChatRoom and ChatMessage models, which handle the storage and
management of chat conversations between customers and sellers.
"""

from django.conf import settings
from django.db import models


class ChatRoom(models.Model):
    """
    Represents a chat room between a customer and a seller.
    """
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='customer_rooms', on_delete=models.CASCADE)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='seller_rooms', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the chat room.
        """
        return f"ChatRoom between {self.customer.first_name} and {self.seller.first_name}"


class ChatMessage(models.Model):
    """
    Represents a message within a chat room.
    """
    chat_room = models.ForeignKey(ChatRoom, related_name='messages', on_delete=models.CASCADE)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a brief representation of the message content and its timestamp.
        """
        return f'Message in {self.chat_room} at {self.timestamp}: {self.message[:50]}'

