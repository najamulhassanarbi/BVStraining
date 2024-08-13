"""
File: urls.py

Description:
    Defines the URL patterns for the Products app, mapping views to their respective paths.
    This includes routes for listing products, viewing product details, managing the cart,
    and proceeding to checkout.
"""
from django.urls import path
from products.views import ProductListView, ProductDetailView, CheckoutView, CartView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
]
