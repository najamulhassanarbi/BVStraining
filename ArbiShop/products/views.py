"""
File: views.py

Description:
    Contains the view classes for the Products app, managing the display and interaction
    with product listings, product details, the shopping cart, and the checkout process.
    The views are implemented using Django's generic class-based views, with some requiring
    user authentication for access.
"""
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django_filters.views import FilterView

from products.forms import ReviewForm
from products.models import Product, Category, Review, Wishlist
from products.filters import ProductFilter
from products.utils import get_config_value, user_can_review_product


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
    paginate_by = 10

    def get_queryset(self):
        """
        Create Query for filtering
        """
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        """
        fetches the data and provide context data to the template
        """
        context = super().get_context_data(**kwargs)
        context['featured_categories'] = Category.objects.filter(featured=True)
        context['categories'] = Category.objects.all()
        wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
        context['wishlists'] = wishlist.products.all()

        return context


class ProductDetailView(DetailView):
    """
    Displays the details of a specific product, including its description, price,
    and other relevant information.
    """
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['reviews'] = Review.objects.filter(product=product).order_by('-created_at')
        context['review_form'] = ReviewForm()
        wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
        context['wishlists'] = wishlist.products.all()

        return context


class CategoryProductsView(FilterView, ListView):
    """
    Shows a paginated and filtered list of products in a category.
    Combines FilterView and ListView to display products in a specific category with filtering.
    Also provides additional context for the current category and all available categories.
    """

    model = Product
    template_name = 'products/category_product_listing.html'
    context_object_name = 'products'
    paginate_by = 10
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
        wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
        context['wishlists'] = wishlist.products.all()
        return context


@method_decorator(login_required, name='dispatch')
@method_decorator(user_can_review_product, name='dispatch')
class ReviewCreateView(CreateView):
    """
    View to handle the creation of a new review by a user.
    - Ensures the user is logged in and eligible to review the product.
    - Associates the review with the current user and product.
    - Redirects to the product detail page upon successful submission.
    """
    model = Review
    form_class = ReviewForm

    def form_valid(self, form):
        """
        Sets the user and product for the review before saving the form.
        Associates the review with the current user and the product specified by 'pk'.
        """
        form.instance.user = self.request.user
        form.instance.product = get_object_or_404(Product, id=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        """
        Returns the URL to redirect to after a successful form submission.
        Redirects to the product detail page of the reviewed product.
        """
        return reverse_lazy('product_detail', kwargs={'pk': self.kwargs['pk']})


class WishlistView(LoginRequiredMixin, ListView):
    template_name = 'wishlist/wishlist.html'
    context_object_name = 'wishlist_items'

    def get_queryset(self):
        wishlist, created = Wishlist.objects.get_or_create(user=self.request.user)
        return wishlist.products.all()


class AddToWishlistView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        wishlist, created = Wishlist.objects.get_or_create(user=request.user)
        wishlist.products.add(product)
        return redirect(reverse_lazy('wishlist'))


class RemoveFromWishlistView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product_id = self.kwargs['product_id']
        product = get_object_or_404(Product, id=product_id)
        wishlist = get_object_or_404(Wishlist, user=request.user)
        wishlist.products.remove(product)
        return redirect(reverse_lazy('wishlist'))
