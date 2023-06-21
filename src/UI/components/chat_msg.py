import modules

from UI.widgets.text.no_scroll_browser import NoScrollTextBrowser
from UI.widgets.label.chat_msg_username import ChatRoomUsername

from src.core.chat_msg_data import ChatMsgData

class ChatMsg(modules.QFrame):
    def __init__(self, msg_info: ChatMsgData= None, parent = None) -> None:
        super().__init__(parent)

        self.layout = modules.QVBoxLayout()

        self.text_box = NoScrollTextBrowser()
        self.user = ChatRoomUsername(msg_info.username)

        self.layout.addWidget(self.user)
        self.layout.addWidget(self.text_box)

        self.setLayout(self.layout)

    def set_text_name(self, name: str):
        self.text_box.setObjectName(name)

    def set_document(self, doc, text):
        self.text_box.setDocument(doc, text)


