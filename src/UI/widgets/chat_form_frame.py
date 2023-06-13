import modules

from UI.widgets.chat_form_join import ChatFormJoin
from UI.widgets.chat_form_create import ChatFormCreate

class ChatFormFrame(modules.QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = modules.QVBoxLayout(self)

        self.create_frame = ChatFormCreate()
        self.join_frame = ChatFormJoin()

        self.layout.addWidget(self.create_frame)
        self.layout.addWidget(self.join_frame)

        self.setLayout(self.layout)

    def create_room_open(self):
        self.join_frame.setVisible(False)
        self.join_frame.username.clear()
        self.join_frame.room_password.clear()
        self.join_frame.room_id.clear()

        self.create_frame.setVisible(True)

    def join_room_open(self):
        self.create_frame.setVisible(False)
        self.create_frame.username.clear()
        self.create_frame.room_password.clear()

        self.join_frame.setVisible(True)


