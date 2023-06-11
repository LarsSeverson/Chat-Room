import modules

from UI.buttons.join_room_button import ExecuteJoinRoomButton

from UI.widgets.text.chat_form_username import FormUsername
from UI.widgets.text.chat_room_password import FormPassword
from UI.widgets.text.chat_form_id import FormID

class ChatFormJoin(modules.QFrame):
    def __init__(self):
        super().__init__()

        self.layout = modules.QVBoxLayout(self)
        self.middle_layout = modules.QHBoxLayout()
        self.bottom_layout = modules.QHBoxLayout()
        
        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(11)  

        self.room_id = FormID()
        self.username = FormUsername()
        self.room_password = FormPassword()
        self.join_room_button = ExecuteJoinRoomButton()

        self.join_room_label = modules.QLabel()
        self.join_room_label.setFont(self.font)
        self.join_room_label.setText('Join')
        self.join_room_label.setMaximumHeight(15)

        self.space_1 = modules.QLabel()
        self.space_2 = modules.QLabel()

        self.middle_layout.addWidget(self.room_id)
        self.middle_layout.addWidget(self.room_password)

        self.bottom_layout.addWidget(self.space_1)
        self.bottom_layout.addWidget(self.join_room_button)
        self.bottom_layout.addWidget(self.space_2)

        self.layout.addWidget(self.username)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)
        self.layout.addWidget(self.join_room_label, 0, modules.Qt.AlignHCenter)
    
    def resizeEvent(self, a0: modules.QResizeEvent) -> None:
        return super().resizeEvent(a0)

