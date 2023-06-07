import modules

from UI.components.chat_room import ChatRoom
from UI.components.chat_box import ChatBox
from UI.components.chat_option import ChatOption

from src.core.chat import ChatType

class ChatUI(modules.QFrame):

    message_received = modules.pyqtSignal(str)

    def __init__(self, central_widget) -> None:
        super().__init__(central_widget)

        self.chat_open = False

        self.setFrameShape(modules.QFrame.StyledPanel)
        self.setFrameShadow(modules.QFrame.Raised)
        self.setStyleSheet('background-color: rgb(240, 240, 240);')

        self.chat_layout = modules.QVBoxLayout()
        self.chat_layout.setObjectName('chat_layout')

        self.chat_option = ChatOption()
        #self.chat_option.option_frame.form_frame.create_frame.create_room_button.clicked.connect(self.open_)

        self.chat_room = ChatRoom(self)

        self.chat_box = ChatBox(self)
        self.chat_box.set_send_callback(self.send_txt_msg)

        self.chat_layout.addWidget(self.chat_room, 0)
        self.chat_layout.addWidget(self.chat_box, 0, modules.Qt.AlignBottom)

        self.setLayout(self.chat_option)

    def resizeEvent(self, a0: modules.QResizeEvent) -> None:
        super().resizeEvent(a0)
        self.chat_box.resize(a0.size().width(), a0.size().height())

    def resize_signal(self, width, height):
        self.chat_box.handle_height()
        #self.chat_box.resize(width, height)

    def send_txt_msg(self, document):
        self.chat_room.add_txt_msg(ChatType.SENDER, document=document)
        self.send_callback(document.toPlainText())

    def receive_txt_msg(self, text: str):
        self.chat_room.add_txt_msg(ChatType.RECEIVER, document=self.chat_box.document(), text=text)

    def open_chat(self):
        self.chat_open = True
        #self.setLayout(self.chat_layout)
        self.setVisible(True)

    def open_option(self):
        self.setLayout(self.chat_option)

    def close(self):
        self.chat_open = False
        self.setVisible(False)

    def set_send_callback(self, func):
        self.send_callback = func
