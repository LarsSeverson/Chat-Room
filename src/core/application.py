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

        self.chat.set_send_callback(self.backend_chat_send_msg)
    
    def start_chat(self):
        self.chat_process = multiprocessing.Process(target=self.chat.create_room(host=True))
        self.chat_process.start()
        self.chat_running = True

    def backend_chat_send_msg(self, message):
        self.window.ui.chat.message_received.emit(message)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
    
    def stop(self):
        if self.chat_running:
            self.chat.quit_room()
            self.chat_process.join()
        self.chat_running = False
