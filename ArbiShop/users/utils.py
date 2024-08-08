import jwt
from datetime import datetime, timedelta
from django.conf import settings


def create_jwt_token(user):
    """
    A function that creates a JWT token for the given user
    :param user:
    :type user:
    :return:
    :rtype:
    """
    payload = {
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow()
    }
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    return token


def decode_jwt_token(token):
    """
    A function that decodes a JWT token
    :param token:
    :type token:
    :return:
    :rtype:
    """
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        return payload['email']
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
