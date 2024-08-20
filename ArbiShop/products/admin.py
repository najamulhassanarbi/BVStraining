# File: products/admin.py

"""
File: products/admin.py

Description:
    Configures the Django Admin for the Products app, including custom forms
    and inline product management within categories.
"""

from django.contrib import admin
from products.models import Product, Category,Config
from products.forms import CategoryForm, ProductForm, ConfigForm


class ProductInline(admin.TabularInline):
    """
    Inline form for managing products within categories in the admin interface.
    """
    model = Product
    form = ProductForm
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    """
    Admin interface for managing categories, with inline product management.
    """
    form = CategoryForm
    inlines = [ProductInline]
    list_display = ['name', 'description', "image", "featured"]
    search_fields = ['name']


class ProductAdmin(admin.ModelAdmin):
    """
    Admin interface for managing products with custom list view and filters.
    """
    form = ProductForm
    list_display = ['name', 'price', 'stock', 'seller', 'category', 'is_active', 'created_at']
    search_fields = ['name', 'category__name', 'seller__username']
    list_filter = ['category', 'is_active']
    date_hierarchy = 'created_at'


class ConfigAdmin(admin.ModelAdmin):
    """
    Admin interface for managing configs
    """
    form = ConfigForm
    list_display = ['key', 'value']
    search_fields = ['key']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Config, ConfigAdmin)
