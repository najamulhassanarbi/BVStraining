"""
urls.py

Defines URL patterns for the seller app, including routes for the seller dashboard,
product management, and order items.
"""

from django.urls import path

from seller.views import (
    AddProductView,
    UpdateProductView,
    DeleteProductView,
    SellerDashboardView,
    SellerOrderItemsView
)

app_name = 'seller'

urlpatterns = [
    path('dashboard/', SellerDashboardView.as_view(), name='dashboard'),
    path('dashboard/orders', SellerOrderItemsView.as_view(), name='orders'),
    path('dashboard/products', SellerDashboardView.as_view(), name='products'),
    path('dashboard/add-product/', AddProductView.as_view(), name='add_product'),
    path('dashboard/update-product/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
    path('dashboard/delete-product/<int:pk>/', DeleteProductView.as_view(), name='delete_product'),
]
