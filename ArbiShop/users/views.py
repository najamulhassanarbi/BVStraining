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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib import messages
from django.views.generic import CreateView, UpdateView

from users.forms import CustomUserCreationForm, LoginForm, UserUpdateForm
from users.utils import create_jwt_token

User = get_user_model()




class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """
    Handles user profile updates.
    """
    model = User
    form_class = UserUpdateForm
    template_name = 'users/update_profile.html'
    success_url = reverse_lazy('users:profile')  # Use the appropriate URL name

    def get_object(self):
        """
        Return the current user object.

        :return: User object
        :rtype: User
        """
        return self.request.user

    def form_valid(self, form):
        """
        Process the profile update form and save the user.

        :param form: Validated form
        :type form: UserUpdateForm
        :return: Redirects to profile page or re-renders profile page with success message
        :rtype: HttpResponse
        """
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)


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
        return render(request, 'users/signup.html', {'form': form})

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
        return render(request, 'users/signup.html', {'form': form})


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
        return render(request, 'users/login.html', {'form': form})

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
                user = authenticate(request, username=user, password=password)
                if user:
                    token = create_jwt_token(user)
                    response = redirect('home')
                    response.set_cookie('jwt', token)
                    username = form.cleaned_data.get('username')
                    messages.success(request, f'Account created for {username}')
                    return response
                else:
                    return HttpResponse('Invalid credentials', status=401)
            except User.DoesNotExist:
                return HttpResponse('Invalid credentials', status=401)
        return render(request, 'users/login.html', {'form': form})


class HomeView(View):
    """
    Displays the home page to logged-in users.
    """

    def get(self, request):
        """
        Render the home page for logged-in users.

        :param request: HTTP GET request
        :type request: HttpRequest
        :return: Rendered home page
        :rtype: HttpResponse
        """
        return render(request, 'users/home.html')


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


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/password_reset_email.html'
    subject_template_name = 'users/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('home')



