from modules import QApplication, sys, multiprocessing
from multiprocessing import Pipe

from core.window import Window
from core.chat import Chat

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)

        self.msg_sender_pipe, self.msg_receiver_pipe = Pipe()

        self.window = Window()
        self.chat = Chat()

        self.window.set_text_callback(self.chat.receive_txt_msg)
        self.window.set_msg_receive_pipe(self.msg_receiver_pipe)
        self.window.set_close(self.stop)

        self.chat.set_msg_send_pipe(self.msg_sender_pipe)
        self.chat.set_send_callback(self.window.ui.chat.receive_text_msg)
    
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
