"""
forms.py

Defines forms used in the Orders app, specifically the CheckoutForm for handling
user input during the checkout process.
"""


from django import forms
from orders.models import Order


class CheckoutForm(forms.ModelForm):
    """
    Form for capturing user checkout information.

    Uses the Order model and includes fields for address and payment method.
    Customizes form widgets and labels for better user experience.
    """
    class Meta:
        model = Order
        fields = [
            'address_line_1', 'address_line_2', 'city',
            'state', 'postal_code', 'country', 'payment_method'
        ]
        widgets = {
            'address_line_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 1'}),
            'address_line_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address Line 2 (Optional)'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'City'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'State'}),
            'postal_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Postal Code'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'payment_method': forms.RadioSelect(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'address_line_1': 'Address Line 1',
            'address_line_2': 'Address Line 2',
            'city': 'City',
            'state': 'State',
            'postal_code': 'Postal Code',
            'country': 'Country',
            'payment_method': 'Payment Method',
        }
