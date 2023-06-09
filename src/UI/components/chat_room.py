import modules

from src.core.chat import ChatType

from UI.widgets.text.no_scroll_browser import NoScrollTextBrowser
from UI.components.chat_msg import ChatMsg

class ChatRoom(modules.QScrollArea):
    def __init__(self):
        super().__init__()

        self.scrollarea = modules.QScrollArea()

        self.contents = modules.QWidget()

        self.num_msgs = 0

        self.layout = modules.QVBoxLayout(self.contents)

        self.padding = modules.QSpacerItem(20,40,modules.QSizePolicy.Minimum, modules.QSizePolicy.Expanding)

        self.layout.addItem(self.padding)

        self.setStyleSheet('border: none;')
        self.setWidgetResizable(True)
        self.setWidget(self.contents)
        self.setObjectName('chat_room')

        self.setVisible(True)

    def add_txt_msg(self, type: ChatType, document: modules.QTextDocument, msg_info):
        msg = ChatMsg(msg_info)
        msg.set_document(document.clone(), msg_info.text)

        if type == ChatType.SENDER:
            msg.set_text_name('sender_message')
            self.layout.addWidget(msg, 0, modules.Qt.AlignRight | modules.Qt.AlignBottom)
        else:
            msg.set_text_name('other_message')
            self.layout.addWidget(msg, 0, modules.Qt.AlignLeft | modules.Qt.AlignBottom)
        
        self.num_msgs += 1
    

