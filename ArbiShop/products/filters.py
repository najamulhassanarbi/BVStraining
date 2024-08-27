"""
filters.py

Defines the ProductFilter class, which provides filtering options for the Product model.
This filter allows users to search for products based on their name and price,
with additional options to filter by price range (greater than or less than a specified value).

The filters are implemented using the django-filters library.
"""

import django_filters
from products.models import Product


class ProductFilter(django_filters.FilterSet):
    """
    Provides filtering options for the Product model.

    This filter allows users to search for products by name and price, with options
    to filter by price range (greater than or less than a specified value). The
    filter is implemented using the django-filters library.
    """

    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')

    class Meta:
        """
        Meta options for the ProductFilter.
        """
        model = Product
        fields = ['name', 'price']
