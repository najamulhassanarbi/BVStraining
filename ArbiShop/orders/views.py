"""
views.py

Contains view classes for handling the checkout and payment processes in the Orders app.
Manages user interactions during the purchase process, including form validation, payment
processing with Stripe, and order creation.
"""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from orders.forms import CheckoutForm
from django.views import View
from django.shortcuts import render, redirect
from django.conf import settings
import json

from datetime import datetime
import stripe

from orders.models import OrderItem
from products.models import Product

stripe.api_key = settings.STRIPE_SECRET_KEY


class CheckoutView(LoginRequiredMixin, TemplateView):
    """
    Manages the checkout process.

    Ensures the user is logged in and presents the checkout form where users
    can enter their shipping details. Redirects to the payment processing view
    upon successful form submission.
    """

    template_name = 'products/checkout.html'
    success_url = reverse_lazy('orders:process_payment')


class PaymentView(LoginRequiredMixin, View):
    """
    Handles payment processing using Stripe.

    Validates the checkout form, processes the payment via Stripe, and creates
    the order and associated order items. Provides feedback to the user based
    on the outcome of the payment attempt.
    """

    def get(self, *args, **kwargs):
        """
        Displays the payment form.

        Renders the payment form where the user can enter their payment details.
        """
        form = CheckoutForm()
        return render(self.request, 'orders/payment.html', {'form': form})

    def post(self, *args, **kwargs):
        """
        Processes the payment and creates the order.

        Validates the checkout form, processes the payment through Stripe, and
        creates the order and order items if the payment is successful. Handles
        various Stripe errors and provides appropriate feedback to the user.
        """
        form = CheckoutForm(self.request.POST)
        print(self.request.POST)
        if form.is_valid():
            token = self.request.POST['stripeToken']
            print(token)
            order = form.save(commit=False)
            order.user = self.request.user
            cart_data = self.request.POST.get('cart_data')
            if not cart_data:
                return None, "Cart data is missing."

            try:
                cart_items = json.loads(cart_data)
            except json.JSONDecodeError:
                return None, "Cart data is invalid."
            total_amount = 0
            order_items = []

            for item_id, item in cart_items.items():
                total_amount += item['price'] * item['quantity']
                order_item = OrderItem(
                    order=order,
                    product=Product.objects.get(id=item_id),
                    price=item['price'],
                    quantity=item['quantity']
                )
                order_items.append(order_item)
            try:
                charge = stripe.Charge.create(
                    amount=total_amount,
                    currency="pkr",
                    source=token
                )

                if charge['status'] == 'succeeded':
                    order.stripe_charge_id = charge['id']
                    order.payment_method = "card"
                    order.payment_amount = total_amount
                    order.payment_date = datetime.now()
                    order.status = "paid"

                order.save()
                OrderItem.objects.bulk_create(order_items)

                messages.success(self.request, "Your order was successful!")
                return redirect("orders:order-success")

            except stripe.error.CardError as e:
                body = e.json_body
                err = body.get('error', {})
                messages.warning(self.request, f"{err.get('message')}")
                return redirect("orders:process_payment")

            except stripe.error.RateLimitError as e:
                messages.warning(self.request, "Rate limit error")
                return redirect("orders:process_payment")

            except stripe.error.InvalidRequestError as e:
                print(e)
                messages.warning(self.request, "Invalid parameters")
                return redirect("orders:process_payment")

            except stripe.error.AuthenticationError as e:
                messages.warning(self.request, "Not authenticated")
                return redirect("product-list")

            except stripe.error.APIConnectionError as e:
                messages.warning(self.request, "Network error")
                return redirect("orders:process_payment")

            except stripe.error.StripeError as e:
                messages.warning(
                    self.request, "Something went wrong. You were not charged. Please try again.")
                return redirect("orders:process_payment")

        messages.warning(self.request, "Invalid data received")
        return redirect("orders:process_payment")

