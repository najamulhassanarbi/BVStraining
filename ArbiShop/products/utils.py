"""file: products/utils.py

Description:
            Helper functions for product management.
"""

from products.models import Config


def get_config_value(key, default=None):
    """
    Retrieve the value for a given key from the Config model.
    Returns default if the key is not found.
    """
    try:
        return Config.objects.get(key=key).value
    except Config.DoesNotExist:
        return default
