from modules import socket, select, errno, multiprocessing

from src.core.chat_msg_data import ChatMsgData

HEADER_LENGTH = 10
IP = '127.0.0.1'

class ChatClient:
    def __init__(self, PORT, user) -> None:
        self.msg = ''
            
        self.client_active = True
        self.str_username = user
        self.username = user.encode('utf-8')
        self.username_header = f'{len(self.username):<{HEADER_LENGTH}}'.encode('utf-8')
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.socket.connect((IP, PORT))

        self.socket.setblocking(False)

        self.socket.send(self.username_header + self.username)

    def set_msg_send_callback(self, func):
        self.send_callback = func

    def listen(self):
        while self.client_active:
            message = self.msg
            if message:
                message = message.encode('utf-8')
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
                self.socket.send(message_header + message)
                self.msg = ''

            try:
                while self.client_active:
                    username_header = self.socket.recv(HEADER_LENGTH)

                    if not len(username_header):
                        print('Connection closed')
                        self.close()
                        return

                    username_length = int(username_header.decode('utf-8').strip())
                    username = self.socket.recv(username_length).decode('utf-8')

                    message_header = self.socket.recv(HEADER_LENGTH)
                    message_length = int(message_header.decode('utf-8').strip())
                    message = self.socket.recv(message_length).decode('utf-8')

                    self.send_callback(ChatMsgData(message, username))
            except IOError as e:
                if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
                    print('LOG: Reading error: '.format(str(e)))

                continue

            except Exception as e:
                print('LOG: Reading error: '.format(str(e)))
                continue
    
    def close(self):
        self.client_active = False
        self.socket.close()