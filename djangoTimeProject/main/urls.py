"""file: main/urls.py
    This module is used to define the url patterns for the main app.
"""
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index, name='index' ),
]
