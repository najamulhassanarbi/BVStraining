"""
File: views.py

Description:
    Contains the view classes for the Products app, managing the display and interaction
    with product listings, product details, the shopping cart, and the checkout process.
    The views are implemented using Django's generic class-based views, with some requiring
    user authentication for access.
"""
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django_filters.views import FilterView

from products.models import Product, Category
from products.filters import ProductFilter
from products.utils import get_config_value


class CartView(TemplateView):
    """
    Displays the shopping cart page where users can view the products
    they have added to their cart.
    """
    template_name = 'products/cart.html'


class ProductListView(ListView):
    """
    Displays a paginated list of all products available in the e-commerce platform.
    """
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = get_config_value("PRODUCTS_PER_PAGE")
    print(paginate_by)

    def get_queryset(self):
        """
        Create Query for filtering
        :return:
        :rtype:
        """
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        """
        fetches the data and provide context data to the template
        :param kwargs:
        :type kwargs:
        :return:
        :rtype:
        """
        context = super().get_context_data(**kwargs)
        context['featured_categories'] = Category.objects.filter(featured=True)
        context['categories'] = Category.objects.all()

        return context


class ProductDetailView(DetailView):
    """
    Displays the details of a specific product, including its description, price,
    and other relevant information.
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


class CategoryProductsView(FilterView, ListView):
    """
    Shows a paginated and filtered list of products in a category.

    Combines FilterView and ListView to display products in a specific category with filtering.
    Also provides additional context for the current category and all available categories.
    """

    model = Product
    template_name = 'products/category_product_listing.html'
    context_object_name = 'products'
    paginate_by = get_config_value("PRODUCTS_PER_PAGE")
    filterset_class = ProductFilter

    def get_queryset(self):
        """
        Filters products by the selected category and applies the filter set.
        """
        self.category = get_object_or_404(Category, id=self.kwargs['category_id'])
        queryset = super().get_queryset().filter(category=self.category)
        self.filterset = self.filterset_class(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        """
        Adds the current category, filter set, and all categories to the context.
        """
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        context['filterset'] = self.filterset
        context['categories'] = Category.objects.all()
        return context
