"""
File: products/models.py

Description:
    Defines the database models for the Products app, including the Category and Product models.
    These models represent the categories of products and the individual products available
    in the e-commerce platform.
"""

from django.conf import settings
from django.db import models


class Category(models.Model):
    """
    Represents a category of products in the e-commerce platform.
    Categories help organize products into different sections.
    """
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/", blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    Represents an individual product in the e-commerce platform.
    Products belong to a category and are associated with a seller.
    """
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, max_length=1024)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.name


class Config(models.Model):
    """

    Model to store application configuration settings.
    """
    key = models.CharField(max_length=255, unique=True)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.key}: {self.value}'


class Review(models.Model):
    """
    Model representing a product review submitted by a user.
    - Associates the review with a product and a user.
    - Includes a rating, an optional comment, and a timestamp for when the review was created.
    - Automatically deletes reviews if the associated product is deleted.
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Returns a string representation of the review, including the user's name,
        the product name, and the rating.
        """
        return f'{self.user.first_name} {self.user.last_name} - {self.product.name} - {self.rating} stars'
