from PyQt5 import QtGui
import modules
from UI.components.chat_room_ui import ChatRoom
from UI.components.chat_box_ui import ChatBox

from src.core.chat import ChatType

class ChatUI(modules.QFrame):
    def __init__(self, central_widget) -> None:
        super().__init__(central_widget)

        self.chat_open = False

        self.layout = modules.QVBoxLayout()
        self.layout.setObjectName('chat_layout')

        self.setFrameShape(modules.QFrame.StyledPanel)
        self.setFrameShadow(modules.QFrame.Raised)
        self.setStyleSheet('background-color: rgb(240, 240, 240);')

        self.chat_layout = modules.QVBoxLayout(self)
        self.chat_layout.setObjectName('chat_layout')

        self.layout.addWidget(self)

        self.chat_room = ChatRoom(self)

        self.chat_box = ChatBox(self)
        self.chat_box.set_send_callback(self.send_txt_msg)

        self.chat_layout.addWidget(self.chat_room, 0)
        self.chat_layout.addWidget(self.chat_box, 0, modules.Qt.AlignBottom)

    def resizeEvent(self, a0: modules.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.chat_box.resize(a0.size().width(), a0.size().height())

    def resize_signal(self, width, height):
        self.chat_box.handle_height()
        #self.chat_box.resize(width, height)

    def send_txt_msg(self, text):
        self.chat_room.add_txt_msg(ChatType.SENDER, text)
        self.text_callback(text.toPlainText())

    def get_layout(self):
        return self.layout

    def open(self):
        self.chat_open = True
        self.setVisible(True)

    def close(self):
        self.chat_open = False
        self.setVisible(False)

    def set_text_callback(self, func):
        self.text_callback = func
