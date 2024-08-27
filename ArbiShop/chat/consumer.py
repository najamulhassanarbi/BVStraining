"""
WebSocket consumer for handling real-time chat functionality for sellers.

This module defines the SellerChatConsumer class, which manages WebSocket connections
for sellers, including joining chat rooms, receiving and sending messages, and saving
messages to the database.
"""

import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async


class SellerChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        """
        Handles WebSocket connection. Joins the user to the room group based on the room_id.
        """
        self.user = self.scope['user']
        self.room_group_name = self.scope['url_route']['kwargs']['room_id']

        # Join the seller's group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """
        Handles WebSocket disconnection. Removes the user from the room group.
        """
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        """
        Handles receiving a message from the WebSocket. Sends the message to the group
        and saves it to the database.
        """
        data = json.loads(text_data)
        message = data['message']
        user = data['username']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'sendMessage',
                'message': message,
                'user': user,
            }
        )

    async def sendMessage(self, event):
        """
        Handles sending a message to the WebSocket. Broadcasts the message to the client.
        """
        message = event['message']
        customer = event['user']
        await self.send(text_data=json.dumps({
            'message': message,
            'customer': customer,
        }))
        await self.save_message(self.room_group_name, message)

    @database_sync_to_async
    def save_message(self, room_id, message):
        """
        Saves the message to the ChatMessage model in the database.

        Args:
            room_id (str): The ID of the chat room.
            message (str): The message text to save.
        """
        from chat.models import ChatRoom, ChatMessage
        chat_room = ChatRoom.objects.get(id=room_id)
        ChatMessage.objects.create(chat_room=chat_room, message=message)
