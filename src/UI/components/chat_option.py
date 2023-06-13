import modules

from UI.components.chat_option_frame import ChatOptionFrame

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

    def can_create(self) -> bool:
        return self.option_frame.form_frame.create_frame.can_create()
    def can_join(self) -> bool:
        return self.option_frame.form_frame.join_frame.can_join()
    def get_user(self) -> str:
        return self.option_frame.form_frame.create_frame.username.text()
    def get_port(self) -> int:
        return int(self.option_frame.form_frame.join_frame.room_id.text())