from django.conf.urls import url
from chat.consumers import ClientConsumer

websocket_urlpatterns = [
    url('ws/chat/', ClientConsumer),
]