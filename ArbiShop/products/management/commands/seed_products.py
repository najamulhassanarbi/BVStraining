"""
File: products/management/commands/seed_products.py

Description:
    This management command seeds the database with categories and products from a JSON file.
    It reads data from 'cleaned_products.json', creates or retrieves categories, and adds
    products to the database with their associated categories.

    - The command also converts product prices to decimal values.
    - It outputs success messages for each product added to the database.
"""

import json
from django.core.management.base import BaseCommand
from products.models import Category, Product


class Command(BaseCommand):
    """
    A custom Django management command to seed the database with products and categories.
    It reads data from a JSON file, ensuring categories exist or are created,
    and then populates the database with products linked to these categories.
    """
    help = 'Seed the database with products and categories'

    def handle(self, *args, **kwargs):
        with open('cleaned_products.json', 'r') as file:
            data = json.load(file)

        for item in data:
            category_name = item['category']
            category, created = Category.objects.get_or_create(
                name=category_name,
                defaults={'description': f'Description for {category_name}'}
            )

            price = float(item['price'])

            product = Product.objects.create(
                name=item['name'],
                description=item['description'],
                price=price,
                stock=10,
                seller_id=1,
                category=category,
                is_active=True,
                image=item['image_url'],
            )

            self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.name}'))
