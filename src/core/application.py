from modules import QApplication, sys, multiprocessing

from core.window import Window
from core.chat import Chat

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = Window()
        self.chat = Chat()

        self.window.set_text_callback(self.chat.receive_txt_msg)
        self.window.set_close(self.stop)

        self.chat.set_send_callback(self.backend_chat_send_msg)
    
    def start_chat(self):
        self.chat_process = multiprocessing.Process(target=self.chat.create_room(host=True))
        self.chat_process.start()

    def backend_chat_send_msg(self, message):
        self.window.ui.chat.message_received.emit(message)

    def run(self):
        self.window.show()
        self.start_chat()
        sys.exit(self.app.exec_())
    
    def stop(self):
        self.chat.quit_room()
        self.chat_process.join()
