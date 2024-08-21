"""
seller/views.py

Contains views for managing the seller dashboard, products, and order items.
Includes class-based views for listing, creating, updating, and deleting products,
as well as viewing items ordered by customers.
"""

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
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
    success_url = reverse_lazy('seller_dashboard')

    def form_valid(self, form):
        """Set the seller of the product before saving."""
        form.instance.seller = self.request.user
        return super().form_valid(form)


class UpdateProductView(LoginRequiredMixin, UpdateView):
    """View for updating an existing product by the seller."""
    model = Product
    form_class = ProductForm
    template_name = 'seller/manage_product.html'
    success_url = reverse_lazy('seller_dashboard')

    def get_queryset(self):
        """Return the product filtered by the logged-in seller."""
        seller = self.request.user
        return Product.objects.filter(seller=seller)


class DeleteProductView(LoginRequiredMixin, DeleteView):
    """View for deleting a product by the seller."""
    model = Product
    template_name = 'seller/delete_product.html'
    success_url = reverse_lazy('seller_dashboard')

    def get_queryset(self):
        """Return the product filtered by the logged-in seller."""
        seller = self.request.user
        return Product.objects.filter(seller=seller)
