"""file: users/authentication.py
    - This file make a custom backend for authenticating users

"""

from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User
from users.utils import decode_jwt_token


class JWTAuthenticationBackend(BaseBackend):
    """
    Custom Backend that encodes JWT tokens using JWT Authorization header.
    """
    def authenticate(self, request, token=None):
        """
        Authenticate a user with JWT token.
        :param request:
        :type request:
        :param token:
        :type token:
        :return:
        :rtype:
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
        Get a user by ID.
        :param user_id:
        :type user_id:
        :return:
        :rtype:
        """
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
