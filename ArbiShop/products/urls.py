"""
File: urls.py

Description:
    Defines the URL patterns for the Products app, mapping views to their respective paths.
    This includes routes for listing products, viewing product details, managing the cart,
    and proceeding to checkout.
"""
from django.urls import path, include
from products.views import ProductListView, ProductDetailView, CartView, CategoryProductsView

app_name = ''

urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/<int:category_id>/', CategoryProductsView.as_view(), name='category-products'),

    path('cart/', CartView.as_view(), name='cart'),
    path('orders/', include('orders.urls')),  # Include the orders app URLs
]
