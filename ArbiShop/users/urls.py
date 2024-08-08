"""file: main/urls.py
    This module is used to define the url patterns for the main app.
"""

from django.urls import path
from users.views import SignUpView, LoginView, HomeView, LogoutView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', HomeView.as_view(), name='home'),
]
