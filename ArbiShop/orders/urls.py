"""
urls.py

Defines URL patterns for the Orders app, mapping views to routes for checkout,
payment processing, and order success.
"""

from django.urls import path
from django.views.generic import TemplateView

from orders.views import CheckoutView, PaymentView

app_name = 'orders'
urlpatterns = [
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('process-payment/', PaymentView.as_view(), name='process_payment'),
    path('order-success/', TemplateView.as_view(template_name='orders/order_success.html'), name='order_success'),
]
