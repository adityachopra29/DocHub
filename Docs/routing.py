from django.urls import re_path 
from . import consumer

websocket_urlpatterns = [
    re_path(r'https://localhost:8000', consumer.PageConsumer.as_asgi())
]