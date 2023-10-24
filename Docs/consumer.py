import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync

class PageConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        print("connected by the websocket")

    def disconnect(self, code):
        pass

        