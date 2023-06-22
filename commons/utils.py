import jwt
import os
from django.conf import settings


def make_token(username):  # 生存TOKEN
    exp = settings.JWT_AUTH["JWT_REFRESH_EXPIRATION"]
    key = settings.JWT_AUTH["JWT_KEY"]
    payload = {'username': username, 'avatar': 'http://127.0.0.1/static/img/avatar.gif'}

    return jwt.encode(payload, key, algorithm='HS256')
