import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
import modules

from UI.buttons.create_room_button import CreateRoomButton
from UI.buttons.join_room_button import JoinRoomButton

class ChatFormJoin(modules.QFrame):
    def __init__(self):
        super().__init__()

        self.layout = modules.QVBoxLayout(self)

        self.username = modules.QTextEdit()
        self.room_id = modules.QTextEdit()
        self.room_password = modules.QTextEdit()
        self.join_room = modules.QPushButton(self)

        self.username.setSizePolicy     (modules.QSizePolicy.Expanding, modules.QSizePolicy.Fixed)
        self.room_id.setSizePolicy      (modules.QSizePolicy.Expanding, modules.QSizePolicy.Fixed)
        self.room_password.setSizePolicy(modules.QSizePolicy.Expanding, modules.QSizePolicy.Fixed)
        self.join_room.setSizePolicy    (modules.QSizePolicy.Expanding, modules.QSizePolicy.Fixed)

        self.username.setStyleSheet('''
        border-radius: 15px;
        background-color: black;
        ''')
        self.room_id.setStyleSheet('''
        border-radius: 15px;
        background-color: black;
        ''')
        self.room_password.setStyleSheet('''
        border-radius: 15px;
        background-color: black;
        ''')

        self.layout.addWidget(self.username)
        self.layout.addWidget(self.room_id)
        self.layout.addWidget(self.room_password)
        self.layout.addWidget(self.join_room)

class ChatFormCreate(modules.QFrame):
    def __init__(self):
        super().__init__()


class ChatFormFrame(modules.QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.layout = modules.QVBoxLayout(self)

        self.create_frame = ChatFormCreate()
        self.join_frame = ChatFormJoin()

        self.layout.addWidget(self.create_frame)
        self.layout.addWidget(self.join_frame)

        self.setLayout(self.layout)

        self.create_room_open()

    def create_room_open(self):
        self.create_frame.setVisible(True)
        self.join_frame.setVisible(False)

    def join_room_open(self):
        self.create_frame.setVisible(False)
        self.join_frame.setVisible(True)


class ChatOptionFrame(modules.QFrame):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.layout = modules.QVBoxLayout(self)
        self.layout.setObjectName('main_layout')

        self.option_layout = modules.QHBoxLayout()
        self.option_layout.setObjectName('option_layout')

        self.font = modules.QFont()
        self.font.setFamily('Comic Sans MS')
        self.font.setPointSize(11)

        self.form_frame = ChatFormFrame()

        self.create_room = CreateRoomButton()
        self.join_room = JoinRoomButton()

        self.create_room.clicked.connect(self.open_create)
        self.join_room.clicked.connect(self.open_join)

        self.create_room.setFont(self.font)
        self.join_room.setFont(self.font)

        self.create_room.setText('Create Room')
        self.join_room.setText('Join Room')

        self.option_layout.addWidget(self.create_room)
        self.option_layout.addWidget(self.join_room)

        self.layout.addLayout(self.option_layout)
        self.layout.addWidget(self.form_frame)

        self.setStyleSheet('''
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        ''')

        self.setLayout(self.layout)

    def open_create(self):
        self.create_room.open()
        self.form_frame.create_room_open()
        self.join_room.close()

    def open_join(self):
        self.create_room.close()
        self.form_frame.join_room_open()
        self.join_room.open()

class ChatOption(modules.QGridLayout):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.option_frame = ChatOptionFrame()

        self.padding1 = modules.QLabel()
        self.padding2 = modules.QLabel()
        self.padding3 = modules.QLabel()
        self.padding4 = modules.QLabel()

        self.padding1.setMaximumHeight(100)
        self.padding4.setMaximumHeight(100)

        self.addWidget(self.padding1, 0, 1, 1, 1)
        self.addWidget(self.padding2, 1, 0, 1, 1 )
        self.addWidget(self.option_frame, 1, 1, 1, 1)
        self.addWidget(self.padding3, 1, 2, 1, 1 )
        self.addWidget(self.padding4, 2, 1, 1, 1)