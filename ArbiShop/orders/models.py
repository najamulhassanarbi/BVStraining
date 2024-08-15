"""
models.py

Defines the models for the Orders app, including Order and OrderItem.
These models represent customer orders and the items within those orders,
capturing details such as order status, payment information, and shipping address.
"""

from django.db import models
from django.conf import settings
from products.models import Product

from django_countries.fields import CountryField


class Order(models.Model):
    """
    Represents a customer order.

    Stores information about the user who placed the order, the status of the order,
    payment details, and shipping address. The Order model is linked to the OrderItem
    model, which stores details about the individual products in the order.

    Attributes:
        user (ForeignKey): The user who placed the order.
        created_at (DateTimeField): The date and time when the order was created.
        updated_at (DateTimeField): The date and time when the order was last updated.
        status (CharField): The current status of the order.
        stripe_charge_id (CharField): The Stripe charge ID associated with the order.
        payment_method (CharField): The payment method used for the order.
        payment_amount (DecimalField): The total payment amount for the order.
        payment_date (DateTimeField): The date and time when the payment was made.
        total_amount (DecimalField): The total amount for the order, including all items.
        address_line_1 (CharField): The first line of the shipping address.
        address_line_2 (CharField): The second line of the shipping address (optional).
        city (CharField): The city of the shipping address.
        state (CharField): The state of the shipping address.
        postal_code (CharField): The postal code of the shipping address.
        country (CountryField): The country of the shipping address.
    """

    STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('processing', 'Processing'),
        ('paid', 'Paid'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='placed')

    stripe_charge_id = models.CharField(max_length=255, blank=True, null=True)
    payment_method = models.CharField(max_length=50, blank=True, null=True)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    payment_date = models.DateTimeField(blank=True, null=True)

    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = CountryField(blank_label='Select Country')

    def __str__(self):
        return f"Order {self.id} by {self.user.email}"


class OrderItem(models.Model):
    """
    Represents an individual item within an order.

    Stores information about the product, the quantity ordered, and the price at which
    the product was sold. Each OrderItem is linked to an Order, and multiple OrderItems
    can be associated with a single Order.

    Attributes:
        order (ForeignKey): The order that this item belongs to.
        product (ForeignKey): The product that was ordered.
        quantity (PositiveIntegerField): The quantity of the product ordered.
        price (DecimalField): The price of the product at the time of the order.
    """
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in order {self.order.id} having price {self.price}"
