"""
File: products/management/commands/clear_data.py

Description:
    Custom management command for the Products app that deletes all entries from
    the Product and Category tables. This command is useful for clearing out data
    during development or testing phases.
"""

from django.core.management.base import BaseCommand
from products.models import Product, Category


class Command(BaseCommand):
    """
    Deletes all data from the Product and Category tables in the database.
    This command is executed using the Django management command system.
    """
    help = 'Deletes all data from the Product and Category tables'

    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all data from Product and Category tables.'))
