from channels.generic.websocket import WebsocketConsumer
import json
from rest_framework_jwt.utils import jwt_decode_handler
from django.contrib.auth.models import User

class ClientConsumer(WebsocketConsumer):
    # 记录已经连接消息系统的所有客户端
    clientList = []

    def connect(self):
        self.accept()
        # 防止客户端没有正常退出导致状态不正确
        for i in range(len(ClientConsumer.clientList)):
            if ClientConsumer.clientList[i]["client"].scope["client"][0] == self.scope['client'][0]:
                del (ClientConsumer.clientList[i])
                break

        # 保存当前正在连接消息系统的客户端
        itemClient = {"client": self}
        # 记录所有已经连接的客户端

        ClientConsumer.clientList.append(itemClient)

    def disconnect(self, close_code):

        for i in range(len(ClientConsumer.clientList)):

            if ClientConsumer.clientList[i]["client"].scope["client"][0] == self.scope['client'][0]:
                del (ClientConsumer.clientList[i])
                break

    def receive(self, text_data):
        token = self.scope['cookies']['Authorization']
        ustr = jwt_decode_handler(token)
        user = User.objects.get(username=ustr['username'])

        message = '服务端返回数据：' + text_data

        for i in range(len(ClientConsumer.clientList)):
            ClientConsumer.clientList[i]['client'].send(message)




