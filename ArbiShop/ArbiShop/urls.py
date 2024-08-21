"""
file:urls.py
    This module defines the url patterns for the djangoTimeProject application.
    URL configuration for ArbiShop project.
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('users/', include('users.urls')),
                  path('', include('products.urls')),
                  path('password-reset-complete/',
                       auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
                       name='password_reset_complete'),
                  path('seller/', include('seller.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
