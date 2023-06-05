import modules

from UI.buttons.create_room_button import CreateRoomButton
from UI.buttons.join_room_button import JoinRoomButton

class ChatOptionFrame(modules.QFrame):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.layout = modules.QVBoxLayout()

        self.create_room = CreateRoomButton()
        self.join_room = JoinRoomButton()

        self._or = modules.QLabel()
        self._or.setMaximumHeight(10)
        self._or.setText('or')

        self.layout.addWidget(self.create_room)
        self.layout.addWidget(self._or)
        self.layout.addWidget(self.join_room)

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