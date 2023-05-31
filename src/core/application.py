from modules import QApplication, sys, multiprocessing

from core.window import Window
from core.chat import Chat

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.window = Window()
        self.chat = Chat()

        self.window.set_text_callback(self.chat.en_queue)
        self.window.set_close(self.stop)

    def start_chat(self):
        self.chat_process = multiprocessing.Process(target=self.chat.create_room(host=True))
        self.chat_process.start()

    def run(self):
        self.window.show()
        self.start_chat()
        sys.exit(self.app.exec_())
    
    def stop(self):
        self.chat.quit_room()
        self.chat_process.join()
