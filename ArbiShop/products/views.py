"""
File: views.py

Description:
    Contains the view classes for the Products app, managing the display and interaction
    with product listings, product details, the shopping cart, and the checkout process.
    The views are implemented using Django's generic class-based views, with some requiring
    user authentication for access.
"""

from django.views.generic import ListView, DetailView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from products.models import Product
from products.filters import ProductFilter


class CartView(TemplateView):
    """
    Displays the shopping cart page where users can view the products
    they have added to their cart.
    """
    template_name = 'products/cart.html'


class CheckoutView(LoginRequiredMixin, TemplateView):
    """
    Handles the checkout process, ensuring the user is logged in before
    allowing them to proceed with purchasing the items in their cart.
    """
    template_name = 'products/checkout.html'
    success_url = reverse_lazy('products:checkout')


class ProductListView(ListView):
    """
    Displays a paginated list of all products available in the e-commerce platform.
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ProductDetailView(DetailView):
    """
    Displays the details of a specific product, including its description, price,
    and other relevant information.
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
