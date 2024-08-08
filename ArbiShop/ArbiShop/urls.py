"""
file:urls.py
    This module defines the url patterns for the djangoTimeProject application.
    URL configuration for ArbiShop project.
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('', include('users.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
