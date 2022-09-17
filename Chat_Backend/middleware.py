from urllib.parse import parse_qs
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from channels.sessions import CookieMiddleware
from rest_framework_simplejwt.tokens import AccessToken,TokenError
from django.contrib.auth.models import AnonymousUser
from channels.db import database_sync_to_async
User = get_user_model()

@database_sync_to_async
def get_user(user_id):
    user =get_object_or_404(User, id=user_id)
    if  user is not None:
        return user
    else:
        return AnonymousUser()

class AuthJWTMiddleware:
    def __init__(self, inner):
        self.inner = inner
    async def __call__(self, scope, receive, send):
        
        try:
            access_token = await AccessToken(scope["cookies"].get('__access')).get('user_id')
            scope['user'] = await get_user(access_token)
        except TokenError:
            scope["user"] = AnonymousUser()
        return await self.inner(scope, receive, send)

def AuthMiddleStack(inner):
    return CookieMiddleware(AuthJWTMiddleware(inner))