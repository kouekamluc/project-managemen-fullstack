from django.urls import re_path
from tasks import consumers

websocket_urlpatterns = [
    re_path(r'ws/socket.io/', consumers.MyConsumer.as_asgi()),
]