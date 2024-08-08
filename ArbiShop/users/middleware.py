from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .utils import decode_jwt_token

User = get_user_model()


class JWTAuthenticationMiddleware(MiddlewareMixin):
    """
    This class defines a custom JWT Authentication middleware
    """
    def process_request(self, request):
        """
        A function to process the JWT Authentication request.
        :param request:
        :type request:
        :return:
        :rtype:
        """
        token = request.COOKIES.get('jwt')
        if token:
            email = decode_jwt_token(token)
            if email:
                try:
                    user = User.objects.get(email=email)
                    request.user = user
                except User.DoesNotExist:
                    pass
