import modules

from UI.buttons.create_room_button import CreateRoomButton
from UI.buttons.join_room_button import JoinRoomButton

class ChatOptionFrame(modules.QFrame):

    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.layout = modules.QGridLayout(self)

        self.font = modules.QFont()
        self.font.setFamily('Comic Sans MS')
        self.font.setPointSize(11)

        self.create_room = CreateRoomButton()
        self.join_room = JoinRoomButton()
        self._or = modules.QLabel()

        self.create_room.setFont(self.font)
        self.join_room.setFont(self.font)
        self._or.setFont(self.font)

        self.create_room.setText('Create Room')
        self.join_room.setText('Join Room')

        self._or.setMaximumHeight(12)
        self._or.setText('or')

        self.layout.addWidget(self.create_room, 1, 0, 1, 1)
        self.layout.addWidget(self._or, 2, 0, 1, 1, modules.Qt.AlignHCenter)
        self.layout.addWidget(self.join_room, 3, 0, 1, 1)

        self.setStyleSheet('''
        background-color: white;
        border-radius: 15px;
        padding: 20px;
        ''')
        self.setLayout(self.layout)

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