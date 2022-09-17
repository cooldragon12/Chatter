"""
ASGI config for Chatter project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from Chat_Backend.middleware import AuthMiddleStack

from Chat_Backend.routing import websocket_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Chatter.settings')
django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http":django_asgi_app,
    "websocket":AuthMiddleStack(
        URLRouter(
            websocket_urlpatterns
        )
    )
})
