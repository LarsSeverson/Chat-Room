import modules

from UI.buttons.create_room_button import CreateRoomButton
from UI.buttons.join_room_button import JoinRoomButton

from UI.widgets.chat_form_frame import ChatFormFrame

class ChatOptionFrame(modules.QFrame):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.layout = modules.QVBoxLayout(self)
        self.layout.setObjectName('main_layout')

        self.option_layout = modules.QHBoxLayout()
        self.option_layout.setObjectName('option_layout')

        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(11)

        self.form_frame = ChatFormFrame()

        self.create_room = CreateRoomButton()
        self.join_room = JoinRoomButton()

        self.line = modules.QFrame()
        self.line.setFrameShape(modules.QFrame.HLine)
        self.line.setFrameShadow(modules.QFrame.Sunken)
        self.line.setStyleSheet('background-color:rgb(227, 227, 227);')

        self.spacer = modules.QWidget()
        self.spacer.setFixedHeight(20)

        self.create_room.clicked.connect(self.open_create)
        self.join_room.clicked.connect(self.open_join)

        self.create_room.setFont(self.font)
        self.join_room.setFont(self.font)

        self.create_room.setText('Create Room')
        self.join_room.setText('Join Room')

        self.option_layout.addWidget(self.create_room)
        self.option_layout.addWidget(self.join_room)

        self.layout.addLayout(self.option_layout)
        self.layout.addWidget(self.spacer)
        self.layout.addWidget(self.line)
        self.layout.addWidget(self.form_frame)

        self.setStyleSheet('''
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        ''')

        self.setLayout(self.layout)

        self.setFixedHeight(self.size().height())

        self.open_create()

    def open_create(self):
        self.create_room.open()
        self.form_frame.create_room_open()
        self.join_room.close()

    def open_join(self):
        self.create_room.close()
        self.form_frame.join_room_open()
        self.join_room.open()
