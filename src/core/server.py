from modules import socket, select, multiprocessing

HEADER_LENGTH = 10

IP = '127.0.0.1'
PORT = 1234

class ChatServer:
    def __init__(self) -> None:
        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((IP, PORT))
        self.socket.listen()


        self.sockets_list = [self.socket]
        self.clients = {}

        self.server_active = True

        print(f'LOG: Listening for connections on {IP}: {PORT}...')

    def broadcast(self, notif_socket, message):
        user = self.clients[notif_socket]
        print(f'LOG: Received message from {user["data"].decode("utf-8")}: {message["data"].decode("utf-8")}')

        for client_socket in self.clients:
            if client_socket != notif_socket:
                client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])

    def msg_receive(self, client_socket):
        try:
            message_header = client_socket.recv(HEADER_LENGTH)

            if not len(message_header):
                return False
            
            message_length = int(message_header.decode('utf-8').strip())

            return {'header': message_header, 'data': client_socket.recv(message_length)}
        except:
            return False
        
    def run(self):
        while self.server_active:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list)

            for notif_socket in read_sockets:
                if notif_socket == self.socket:
                    # new connection
                    client_socket, client_address = self.socket.accept()

                    user = self.msg_receive(client_socket)
                    if not user:
                        continue

                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                    print('LOG: Accepted new connection from: {}:{}, username: {}'.format(*client_address, user['data'].decode('utf-8')))
                
                else:
                    # new message
                    message = self.msg_receive(notif_socket)

                    if message is False:
                        # client disconnected
                        print('LOG: User disconnected from: {}'.format(self.clients[notif_socket]['data'].decode('utf-8')))

                        self.sockets_list.remove(notif_socket)

                        del self.clients[notif_socket]

                        continue
                    
                    self.broadcast(notif_socket, message)

            for notif_socket in exception_sockets:
                self.sockets_list.remove(notif_socket)
                del self.clients[notif_socket]

    def close(self):
        self.server_active = False
        self.socket.close()