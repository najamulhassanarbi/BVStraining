"""
seller/views.py

Contains views for managing the seller dashboard, products, and order items.
Includes class-based views for listing, creating, updating, and deleting products,
as well as viewing items ordered by customers.
"""
from django.core.exceptions import PermissionDenied
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from chat.models import ChatRoom
from products.models import Product
from orders.models import OrderItem
from seller.forms import ProductForm


class SellerDashboardView(LoginRequiredMixin, ListView):
    """View for displaying the seller's product listing dashboard."""
    model = Product
    template_name = 'seller/product_listing.html'
    context_object_name = 'seller_products'
    paginate_by = 10

    def get_queryset(self):
        """Return products filtered by the logged-in seller."""
        seller = self.request.user
        return Product.objects.filter(seller=seller)

    def get_context_data(self, **kwargs):
        """Add additional context data for the seller's products."""
        context = super().get_context_data(**kwargs)
        seller_products = self.get_queryset()
        context['seller_products'] = seller_products
        return context


class SellerOrderItemsView(LoginRequiredMixin, ListView):
    """View for displaying items ordered from the seller."""
    model = OrderItem
    template_name = 'seller/orders_listing.html'
    context_object_name = 'seller_products'
    paginate_by = 10

    def get_queryset(self):
        """Return order items filtered by the logged-in seller."""
        return OrderItem.objects.filter(product__seller=self.request.user).select_related('product', 'order')


class AddProductView(LoginRequiredMixin, CreateView):
    """View for adding a new product by the seller."""
    model = Product
    form_class = ProductForm
    template_name = 'seller/manage_product.html'
    success_url = reverse_lazy('seller:dashboard')

    def form_valid(self, form):
        """Set the seller of the product before saving."""
        form.instance.seller = self.request.user
        return super().form_valid(form)


class UpdateProductView(LoginRequiredMixin, UpdateView):
    """View for updating an existing product by the seller."""
    model = Product
    form_class = ProductForm
    template_name = 'seller/manage_product.html'
    success_url = reverse_lazy('seller:dashboard')

    def get_queryset(self):
        """Return the product filtered by the logged-in seller."""
        seller = self.request.user
        return Product.objects.filter(seller=seller)


class DeleteProductView(LoginRequiredMixin, DeleteView):
    """View for deleting a product by the seller."""
    model = Product
    template_name = 'seller/delete_product.html'
    success_url = reverse_lazy('seller:dashboard')

    def get_queryset(self):
        """Return the product filtered by the logged-in seller."""
        seller = self.request.user
        return Product.objects.filter(seller=seller)


class SellerChatsView(LoginRequiredMixin, TemplateView):
    """
    Displays all available chat rooms for the logged-in seller.
    """
    template_name = 'seller/chats_listing.html'

    def get_context_data(self, **kwargs):
        """
        Adds the seller's chat rooms to the context for rendering in the template.

        Returns:
            dict: The context data containing all chat rooms where the logged-in user is the seller.
        """
        context = super().get_context_data(**kwargs)
        seller = self.request.user
        chat_rooms = ChatRoom.objects.filter(seller=seller).annotate(
            unread_messages=Count('messages', filter=Q(messages__is_read=False))
        ).order_by('-created_at')
        context['chat_rooms'] = chat_rooms
        return context


class SellerChatRoomView(LoginRequiredMixin, TemplateView):
    """
    View for sellers to join and interact in a chat room.
    """
    template_name = "seller/testin_seller.html"

    def get_context_data(self, **kwargs):
        """
        Ensures the seller is part of the chat room and provides the context data for rendering the template.
        Marks unread messages as read when the seller views the chat room.
        """
        context = super().get_context_data(**kwargs)
        chat_room = get_object_or_404(ChatRoom, id=self.kwargs['room_id'])
        if self.request.user != chat_room.seller:
            raise PermissionDenied("You do not have permission to access this chat room.")
        unread_messages = chat_room.messages.filter(is_read=False)
        unread_messages.update(is_read=True)
        chats = chat_room.messages.all().order_by('timestamp')
        seller = self.request.user
        chat_rooms = ChatRoom.objects.filter(seller=seller).annotate(
            unread_messages=Count('messages', filter=Q(messages__is_read=False))
        ).order_by('-created_at')
        context['chat_rooms'] = chat_rooms
        context['chat_room'] = chat_room
        context['chats'] = chats

        return context
