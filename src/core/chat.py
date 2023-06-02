from modules import threading, Enum

from src.core.client import ChatClient
from src.core.server import ChatServer

class ChatType(Enum):
    SENDER = 1
    RECEIVER = 2

class Chat:
    def __init__(self) -> None:
        self.msg_buf = []

        self.server_active = False

    def create_room(self, host, room_id = 1234):
        if host:
            self.server_active = True
            self.server = ChatServer()
            self.server_thread = threading.Thread(target=self.server.run)
            self.server_thread.start()

        self.client = ChatClient(PORT=room_id)
        self.client.set_outbound_callback(self.msg_outbound)

        self.client_thread = threading.Thread(target=self.client.listen)
        self.client_thread.start()
        
    def quit_room(self):
        self.client.close()
        self.client_thread.join()

        # make sure to close the server last
        if self.server_active:
            self.server.close()
            self.server_thread.join()

    def msg_inbound(self, text):
        #self.msg_buf.append(text)

        self.client.msg = text

    def msg_outbound(self, text):
        print(text)