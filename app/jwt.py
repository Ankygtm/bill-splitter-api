from datetime import datetime, timedelta

import jwt
from django.conf import settings

secret = settings.SECRET_KEY


def generate_jwt(payload: dict, exp_hours: int | float = 24):
    payload['exp'] = datetime.now() + timedelta(hours=exp_hours)
    payload['iat'] = datetime.now()
    return jwt.encode(payload, secret, algorithm='HS256')


def verify_token(token: str):
    try:
        return jwt.decode(token, secret, algorithms=['HS256'])
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None
