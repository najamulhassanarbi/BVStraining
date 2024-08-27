"""
Views for handling chat room interactions in the chat application.

This module defines views for creating or retrieving chat rooms between customers and sellers,
as well as rendering the chat room interface. It ensures that only authorized users (the customer
or seller involved in the chat) can access the chat room and view its messages.
"""

from django.contrib.auth import get_user_model
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from chat.models import ChatRoom

User = get_user_model()


class CreateOrGetChatRoomView(LoginRequiredMixin, RedirectView):
    """
    Handles creating or retrieving a chat room between the logged-in customer and a specified seller.

    If a chat room already exists between the customer and the seller, it is retrieved.
    Otherwise, a new chat room is created, and the user is redirected to the chat room.
    """

    def get_redirect_url(self, *args, **kwargs):
        """
        Constructs the URL to redirect the user to the appropriate chat room.

        Retrieves or creates a ChatRoom instance between the logged-in customer and the seller,
        then redirects the user to the chat room page.

        Returns:
            str: The URL of the chat room.
        """
        seller_id = self.kwargs['seller_id']
        seller = get_object_or_404(User, id=seller_id)
        customer = self.request.user
        chat_room, created = ChatRoom.objects.get_or_create(customer=customer, seller=seller)
        return reverse_lazy('chat_room', kwargs={'room_id': chat_room.id})


class ChatRoomView(LoginRequiredMixin, TemplateView):
    """
    Renders the chat room template, ensuring that only the involved customer or seller can access it.

    This view checks whether the logged-in user is either the customer or the seller associated
    with the chat room. If not, access is denied.
    """
    template_name = 'chat/chat_page.html'

    def get_context_data(self, **kwargs):
        """
        Adds the chat room instance and its associated messages to the template context.

        Ensures the logged-in user is a participant in the chat room. If not, raises a PermissionDenied exception.

        Returns:
            dict: The context data for rendering the template.
        """
        context = super().get_context_data(**kwargs)
        chat_room = get_object_or_404(ChatRoom, id=self.kwargs['room_id'])
        if self.request.user != chat_room.customer and self.request.user != chat_room.seller:
            raise PermissionDenied
        messages = chat_room.messages.all().order_by('timestamp')

        context['chat_room'] = chat_room
        context['messages'] = messages
        return context
