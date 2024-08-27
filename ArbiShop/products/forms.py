"""
File: products/forms.py

Description:
    Custom forms for the Category and Product models used in the Django Admin interface.
"""

from django import forms
from products.models import Product, Category, Config, Review


class CategoryForm(forms.ModelForm):
    """
    Form for managing Category model fields in the admin.
    """

    class Meta:
        model = Category
        fields = ['name', 'description', "image", "featured"]


class ConfigForm(forms.ModelForm):
    """
    Form for managing Config model fields in the admin.
    """

    class Meta:
        model = Config
        fields = ["key", "value"]


class ProductForm(forms.ModelForm):
    """
    Form for managing Product model fields in the admin.
    """

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'seller', 'category', 'is_active', 'image']


class ReviewForm(forms.ModelForm):
    """
    Form for users to submit a review, including a rating and comment,
    with Bootstrap styling applied to the fields.
    """

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 1,
                'max': 5,
                'placeholder': 'Rate between 1 and 5',
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your review here...',
                'rows': 4,
            }),
        }


class ReviewAdminForm(forms.ModelForm):
    """
    Form for admin users to manage reviews, allowing for editing the
    product, rating, user, and comment, with custom styling.
    """

    class Meta:
        model = Review
        fields = ['product', 'rating', 'user', 'comment']
        widgets = {
            'product': forms.Select(
                attrs={'class': 'admin-form-control'}
            ),
            'rating': forms.NumberInput(
                attrs={
                    'class': 'admin-form-control',
                    'min': 1,
                    'max': 5,
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'admin-form-control',
                    'rows': 4,
                }
            ),
        }
