from modules import threading, Enum, random, socket

from src.core.client import ChatClient
from src.core.server import ChatServer

'''
    For now the room_id variable will be simply useless. I'll need to set up
    a database where users from any device can access a range of active servers
    via the servers' unique id. Something for down the road.
'''

class ChatType(Enum):
    SENDER = 1
    RECEIVER = 2

class Chat:
    def __init__(self) -> None:
        self.msg_buf = []

        self.server_active = False
        self.room_active = False

    def create_room(self, host: bool, user: str, room_id: int = 1234):
        if host:
            self.server_active = True
            self.server = ChatServer(server_id=self.gen_unique_id())
            self.server_thread = threading.Thread(target=self.server.run)
            self.server_thread.start()

        # the room_id will essentially just be the port for now. For safety
        # I'll keep it at 1234
        self.client = ChatClient(room_id, user)
        self.client.set_msg_send_callback(self.send_txt_msg)

        self.client_thread = threading.Thread(target=self.client.listen)
        self.client_thread.start()
        self.room_active = True

    def quit_room(self):
        self.client.close()
        self.client_thread.join()

        # make sure to close the server last
        if self.server_active:
            self.server.close()
            self.server_thread.join()

    def receive_txt_msg(self, text):
        if self.room_active:
            self.client.msg = text

    def gen_unique_id(self) -> int:
        return random.randint(1000, 9999)

    def send_txt_msg(self, msg_info):
        self.send_callback(msg_info)
    
    def set_send_callback(self, func):
        self.send_callback = func
