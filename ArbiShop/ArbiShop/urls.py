"""
file:urls.py
    This module defines the url patterns for the djangoTimeProject application.
    URL configuration for ArbiShop project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
]
