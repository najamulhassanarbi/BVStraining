"""file: main/urls.py
    This module is used to define the url patterns for the main app.
"""
from django.urls import path
from main.views import TimeModelFormView

urlpatterns = [
    path('time-entry',TimeModelFormView.as_view(), name='time-entry' ),
]
