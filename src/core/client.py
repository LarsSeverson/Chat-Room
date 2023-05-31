from modules import socket, select, errno, multiprocessing

HEADER_LENGTH = 10
IP = '127.0.0.1'

class ChatClient:
    def __init__(self, PORT) -> None:
        self.client_active = multiprocessing.Event()
        self.msg = ''
        self.username = 'lars'.encode('utf-8')
        self.username_header = f'{len(self.username):<{HEADER_LENGTH}}'.encode('utf-8')
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((IP, PORT))

        self.socket.setblocking(False)

        self.socket.send(self.username_header + self.username)

        self.client_active.set()

    def listen(self):
        while self.client_active.is_set():
            message = self.get_msg()

    def pop_msg(self, text):
        self.msg = text

    def get_msg(self):
        return self.msg
    
    def close(self):
        self.client_active.clear()
        self.socket.close()