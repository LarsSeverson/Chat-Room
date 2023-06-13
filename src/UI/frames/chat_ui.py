import modules

from UI.components.chat_room import ChatRoom
from UI.components.chat_box import ChatBox
from UI.components.chat_option import ChatOption
from UI.components.chat_loading import ChatLoading

from src.core.chat import ChatType

class ChatUI(modules.QFrame):

    message_received = modules.pyqtSignal(str)

    def __init__(self, central_widget) -> None:
        super().__init__()

        self.chat_open = False

        self.setFrameShape(modules.QFrame.StyledPanel)
        self.setFrameShadow(modules.QFrame.Raised)
        self.setStyleSheet('background-color: rgb(240, 240, 240);')

        self.layout_stack = modules.QStackedLayout()

        self.create_option_layout()
        self.create_chat_layout()
        self.create_loading_layout()

        self.layout_stack.setCurrentIndex(0)
        self.setLayout(self.layout_stack)
    def create_option_layout(self):
        self.chat_option = ChatOption()
        self.chat_option.option_frame.form_frame.create_frame.create_room_button.clicked.connect(self.open_chat)
        self.chat_option.option_frame.form_frame.join_frame.join_room_button.clicked.connect(self.open_chat)

        # dummy widget which is necessary for the layout stack
        widget = modules.QWidget()
        widget.setLayout(self.chat_option)
        self.layout_stack.addWidget(widget)

    def create_chat_layout(self):

        self.chat_room = ChatRoom()
        self.chat_box = ChatBox()
        self.chat_box.set_send_callback(self.send_txt_msg)

        self.chat_layout = modules.QVBoxLayout()
        self.chat_layout.addWidget(self.chat_room, 0)
        self.chat_layout.addWidget(self.chat_box, 0, modules.Qt.AlignBottom)

        widget = modules.QWidget()
        widget.setLayout(self.chat_layout)
        self.layout_stack.addWidget(widget)

    def create_loading_layout(self):
        self.chat_loading = ChatLoading()
        self.chat_option.addWidget(self.chat_loading, 1, 1, 1, 1)

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
        if not self.chat_open:
            self.open_option()
        elif self.chat_option.can_create():
            self.layout_stack.setCurrentIndex(1)
            self.start_chat(True, self.chat_option.get_user())
        elif self.chat_option.can_join():

            self.chat_loading.setVisible(True)
            self.chat_option.option_frame.setVisible(False)

            loop = modules.QEventLoop()
            self.chat_loading.check('127.0.0.1', self.chat_option.get_port())
            self.chat_loading.thread.finished.connect(loop.quit)
            loop.exec_()

            if self.chat_loading.success:
                self.layout_stack.setCurrentIndex(1)
                self.start_chat(False, self.chat_option.get_user())
            else:
                self.chat_loading.setVisible(False)
                self.chat_option.option_frame.setVisible(True)

        self.chat_open = True

        self.setVisible(True)

    def open_option(self):
        self.layout_stack.setCurrentIndex(0)
        self.setVisible(True)
        self.chat_open = False

    def close(self):
        self.setVisible(False)

    def set_send_callback(self, func):
        self.send_callback = func
    def set_backend_start_callback(self, func):
        self.start_chat = func
