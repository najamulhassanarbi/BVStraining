"""
File: users/authentication.py

Description:
    Implements a custom authentication backend for authenticating users using JWT tokens.
    The JWTAuthenticationBackend class allows users to be authenticated via a JWT token
    passed in the Authorization header of requests.
"""

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from users.utils import decode_jwt_token

class JWTAuthenticationBackend(BaseBackend):
    """
    Custom authentication backend that authenticates users based on a JWT token.
    The token is decoded to retrieve the user's email, which is then used to
    authenticate the user against the User model.
    """

    def authenticate(self, request, token=None):
        """
        Authenticate a user using a JWT token.

        :param request: The HTTP request containing the JWT token.
        :param token: The JWT token to be used for authentication.
        :return: The authenticated User object, or None if authentication fails.
        """
        if token is None:
            return None
        email = decode_jwt_token(token)
        if email:
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return None
        return None

    def get_user(self, user_id):
        """
        Retrieve a user by their user ID.

        :param user_id: The ID of the user to be retrieved.
        :return: The User object corresponding to the given ID, or None if no such user exists.
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
