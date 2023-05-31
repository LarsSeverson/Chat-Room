from modules import QApplication, sys, threading

from core.window import Window
from core.chat import Chat

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = Window()
        self.chat = Chat()

        self.window.set_text_callback(self.chat.en_queue)

    def start_chat(self):
        self.chat.create_room(host=True)

    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
