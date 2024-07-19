"""file:urls.py
    This module defines the url patterns for the djangoTimeProject application.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("",include("main.urls"),name="main"),
    path('admin/', admin.site.urls),

]
