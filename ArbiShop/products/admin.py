"""
File: products/admin.py

Description:
    Registers the Product and Category models with the Django admin site,
    enabling management of these models through the admin interface.
"""
from django.contrib import admin

from products.models import Product, Category


admin.site.register(Category)
admin.site.register(Product)
