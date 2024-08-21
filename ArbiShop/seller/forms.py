"""
forms.py

Defines forms for managing products in the seller app.
"""

from django import forms
from products.models import Product, Category


class ProductForm(forms.ModelForm):
    """Form for creating and updating products."""

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'category', 'image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Enter product description'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter price'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter stock quantity'
            }),
            'category': forms.Select(attrs={
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label='Select Category',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
