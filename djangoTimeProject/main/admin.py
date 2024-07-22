"""This module is for registering models with django admin
- Time model Registered
"""
from django.contrib import admin

from main.models import TimeModel


admin.site.register(TimeModel)
