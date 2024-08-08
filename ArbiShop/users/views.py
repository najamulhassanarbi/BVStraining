"""
This module handles user authentication views including signup, login, and logout
using Django's authentication system. It also includes a home view that is
protected by login requirements.

Classes:
    SignUpView: Handles user registration.
    LoginView: Handles user login.
    HomeView: Displays the home page to logged-in users.
    LogoutView: Handles user logout.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from users.forms import CustomUserCreationForm, LoginForm
from users.utils import create_jwt_token

User = get_user_model()

class SignUpView(View):
    """
    Handles user registration.
    GET request renders the signup form.
    POST request processes the signup form and creates a new user.
    """

    def get(self, request):
        """
        Render the signup form.

        :param request: HTTP GET request
        :type request: HttpRequest
        :return: Rendered signup form
        :rtype: HttpResponse
        """
        form = CustomUserCreationForm()
        return render(request, 'signup.html', {'form': form})

    def post(self, request):
        """
        Process the signup form and create a new user.

        :param request: HTTP POST request
        :type request: HttpRequest
        :return: Redirects to home page or re-renders signup form with errors
        :rtype: HttpResponse
        """
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            token = create_jwt_token(user)
            response = redirect('home')
            response.set_cookie('jwt', token)
            return response
        return render(request, 'signup.html', {'form': form})


class LoginView(View):
    """
    Handles user login.
    GET request renders the login form.
    POST request processes the login form and authenticates the user.
    """

    def get(self, request):
        """
        Render the login form.

        :param request: HTTP GET request
        :type request: HttpRequest
        :return: Rendered login form
        :rtype: HttpResponse
        """
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        """
        Process the login form and authenticate the user.

        :param request: HTTP POST request
        :type request: HttpRequest
        :return: Redirects to home page or re-renders login form with errors
        :rtype: HttpResponse
        """
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
                print(user)
                user = authenticate(request, username=user, password=password)
                if user:
                    token = create_jwt_token(user)
                    response = redirect('home')
                    response.set_cookie('jwt', token)
                    return response
                else:
                    return HttpResponse('Invalid credentials', status=401)
            except User.DoesNotExist:
                return HttpResponse('Invalid credentials', status=401)
        return render(request, 'login.html', {'form': form})


class HomeView(LoginRequiredMixin, View):
    """
    Displays the home page to logged-in users.
    """

    login_url = '/login/'
    redirect_field_name = 'redirect_to'

    def get(self, request):
        """
        Render the home page for logged-in users.

        :param request: HTTP GET request
        :type request: HttpRequest
        :return: Rendered home page
        :rtype: HttpResponse
        """
        return render(request, 'home.html')


class LogoutView(View):
    """
    Handles user logout.
    GET request logs out the user and redirects to the login page.
    """

    def get(self, request):
        """
        Log out the user and delete the JWT cookie.

        :param request: HTTP GET request
        :type request: HttpRequest
        :return: Redirects to login page
        :rtype: HttpResponse
        """
        response = redirect('login')
        response.delete_cookie('jwt')
        logout(request)
        return response
