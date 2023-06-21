import modules

class ChatRoomUsername(modules.QLabel):
    def __init__(self, username: str):
        super().__init__()

        self.setText(username)