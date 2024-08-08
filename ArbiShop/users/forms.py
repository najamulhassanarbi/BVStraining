"""file: main/forms.py
    This module if for making forms from django model
    class: CustomerUserCreationForm
        - responsible for creating the user
    class:CustomerUserChangeForm
    - responsible for changing the user
    class: LoginForm
    - responsible for logging the user
"""

from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    """
    A class that inherits from UserCreationForm. responsible for creating user form
    """
    class Meta:
        model = User
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    """
    A class that inherits from UserChangeForm. responsible for changing the user form
    """
    class Meta:
        model = User
        fields = ("email",)


class LoginForm(forms.Form):
    """
    A class that inherits from UserCreationForm. responsible for creating user form
    """
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
