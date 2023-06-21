from modules import QApplication, sys, multiprocessing

from core.window import Window
from core.chat import Chat

'''
                                     Application
                                     /        \
 sends and receives from frontend - /          \ - sends and receives messages to / from backend
                                   /            \
                            Backend Chat       UI Chat
'''

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = Window()
        self.chat = Chat()

        self.chat_running = False

        self.window.set_text_callback(self.chat.receive_txt_msg)
        self.window.set_close(self.stop)

        self.window.ui.chat.set_backend_start_callback(self.start_chat)

        self.chat.set_send_callback(self.backend_chat_send_msg)
    
    def start_chat(self, host: bool, username: str = ''):
        self.chat_process = multiprocessing.Process(target=self.chat.create_room(host, user=username))
        self.chat_process.start()
        self.chat_running = True

    def backend_chat_send_msg(self, msg_info):
        self.window.ui.chat.message_received.emit(msg_info)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
    
    def stop(self):
        if self.chat_running:
            self.chat.quit_room()
            self.chat_process.join()
        self.chat_running = False
