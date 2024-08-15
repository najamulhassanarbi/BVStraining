"""
admin.py

Configures Django admin interface for Order and OrderItem models with inline forms.
"""

from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    """
    Inline admin for OrderItem within Order admin.
    """
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    Admin interface for managing Orders.
    Includes inline OrderItem management.
    """
    list_display = ('id', 'user', 'status', 'total_amount', 'payment_method', 'payment_date', 'created_at')
    list_filter = ('status', 'payment_method', 'created_at')
    search_fields = ('user__email', 'id', 'stripe_charge_id')
    inlines = [OrderItemInline]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    """
    Admin interface for managing individual OrderItems.
    """
    list_display = ('order', 'product', 'quantity', 'price')
    search_fields = ('order__id', 'product__name')
