"""file: main/urls.py
    This module is used to define the url patterns for the main app.
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from users.views import SignUpView, LoginView, HomeView, LogoutView, ResetPasswordView, ProfileUpdateView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('profile-update/', ProfileUpdateView.as_view(), name='update_profile'),

    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
]
