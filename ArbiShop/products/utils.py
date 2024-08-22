"""file: products/utils.py

Description:
            Helper functions for product management.
"""

from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from functools import wraps

from products.models import Config, Review
from products.models import Product
from orders.models import OrderItem
from products.constants import CANNOT_REVIEW_OWN_PRODUCT, MUST_PURCHASE_BEFORE_REVIEW, ALREADY_REVIEWED_PRODUCT


def user_can_review_product(view_func):
    """
    Decorator to restrict users from reviewing a product under certain conditions:
    - Users cannot review their own products.
    - Users can only review products they have purchased.
    - Users can only submit one review per product.

    Displays an appropriate error message and redirects to the product detail page
    if any condition is not met.
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['pk'])
        if product.seller == request.user:
            messages.error(request, CANNOT_REVIEW_OWN_PRODUCT)
            return redirect('product-detail', pk=product.id)
        has_purchased = OrderItem.objects.filter(order__user=request.user, product=product).exists()
        if not has_purchased:
            messages.error(request, MUST_PURCHASE_BEFORE_REVIEW)
            return redirect('product-detail', pk=product.id)
        has_reviewed = Review.objects.filter(user=request.user, product=product).exists()
        if has_reviewed:
            messages.error(request, ALREADY_REVIEWED_PRODUCT)
            return redirect('product-detail', pk=product.id)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def get_config_value(key, default=None):
    """
    Retrieve the value for a given key from the Config model.
    Returns default if the key is not found.
    """
    try:
        return Config.objects.get(key=key).value
    except Config.DoesNotExist:
        return default
