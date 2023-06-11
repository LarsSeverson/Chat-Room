import modules

from UI.buttons.create_room_button import ExecuteCreateRoomButton

from UI.widgets.text.chat_form_username import FormUsername
from UI.widgets.text.chat_room_password import FormPassword

class ChatFormCreate(modules.QFrame):
    def __init__(self):
        super().__init__()

        self.layout = modules.QVBoxLayout(self)
        self.middle_layout = modules.QHBoxLayout()
        self.bottom_layout = modules.QHBoxLayout()
        
        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(11)  

        self.username = FormUsername()
        self.room_password = FormPassword()
        self.create_room_button = ExecuteCreateRoomButton()

        self.create_room_label = modules.QLabel()
        self.create_room_label.setFont(self.font)
        self.create_room_label.setText('Create')
        self.create_room_label.setMaximumHeight(15)

        self.space_1 = modules.QLabel()
        self.space_2 = modules.QLabel()

        self.middle_layout.addWidget(self.room_password)

        self.bottom_layout.addWidget(self.space_1)
        self.bottom_layout.addWidget(self.create_room_button)
        self.bottom_layout.addWidget(self.space_2)

        self.layout.addWidget(self.username)
        self.layout.addLayout(self.middle_layout)
        self.layout.addLayout(self.bottom_layout)
        self.layout.addWidget(self.create_room_label, 0, modules.Qt.AlignHCenter)

    def can_create(self) -> bool:
        return self.username.check

    

