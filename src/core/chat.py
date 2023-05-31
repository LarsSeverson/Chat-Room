from modules import threading, Enum

from src.core.client import ChatClient
from src.core.server import ChatServer

class ChatType(Enum):
    SENDER = 1,
    RECEIVER = 2

class Chat:
    def __init__(self) -> None:
        self.msg_buf = []

        self.client = None

        self.server_thread = threading.Thread()
        self.client_thread = threading.Thread()

    def create_room(self, host, room_id = 1234):
        if host:
            self.server = ChatServer()
            self.server_thread = threading.Thread(target=self.server.run)
            self.server_thread.start()

        self.client = ChatClient(PORT=room_id)
        self.client_thread = threading.Thread(target=self.client.listen)
        self.client_thread.start()

    def en_queue(self, text):
        self.msg_buf.append(text)
    
    def send_msg(self):
        self.client.pop_msg(self.msg_buf.pop())