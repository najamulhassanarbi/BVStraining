
"""
File: products/forms.py

Description:
    Custom forms for the Category and Product models used in the Django Admin interface.
"""

from django import forms
from products.models import Product, Category


class CategoryForm(forms.ModelForm):
    """
    Form for managing Category model fields in the admin.
    """

    class Meta:
        model = Category
        fields = ['name', 'description']


class ProductForm(forms.ModelForm):
    """
    Form for managing Product model fields in the admin.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'seller', 'category', 'is_active', 'image']
