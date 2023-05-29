from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget

import modules
from src.core.chat import ChatType

class NoScrollTextBrowser(modules.QTextBrowser):
    def __init__(self, parent = None) -> None:
        super().__init__(parent)

        self.setVerticalScrollBarPolicy(modules.Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(modules.Qt.ScrollBarAlwaysOff)
        self.setReadOnly(True)
        self.setTextInteractionFlags(modules.Qt.TextSelectableByMouse)
        
        self.setStyleSheet(
        f"""
        QTextBrowser {{
            border-radius: 10px;
        }}
            
        #sender_message {{
            background-color: lightblue;
        }}
            
        #other_message {{
            background-color: white;
        }}
        """
        )
        self.setSizePolicy(modules.QSizePolicy.Preferred, modules.QSizePolicy.Fixed) 
        #self.setSizeAdjustPolicy(modules.QTextBrowser.AdjustToContents)

    def wheelEvent(self, e: modules.QWheelEvent) -> None:
        e.ignore()

    def setDocument(self, document: modules.QTextDocument) -> None:
        super().setDocument(document)
    
    def resizeEvent(self, a0: modules.QResizeEvent) -> None:
        super().resizeEvent(a0)
        
        doc_size = self.document().size().toSize()

        print(self.document().size().width())

        self.setFixedHeight(doc_size.height())
        self.setFixedWidth(doc_size.width())

class ChatRoom(modules.QScrollArea):
    def __init__(self, frame=None):
        super().__init__(frame)

        self.contents = modules.QWidget()

        self.num_msgs = 0

        self.layout = modules.QVBoxLayout(self.contents)

        self.padding = modules.QSpacerItem(20,40,modules.QSizePolicy.Minimum, modules.QSizePolicy.Expanding)

        self.layout.addItem(self.padding)

        self.setStyleSheet('border: none;')
        self.setWidgetResizable(True)
        self.setWidget(self.contents)
        self.setObjectName('chat_room')

    def add_txt_msg(self, type: ChatType, document: modules.QTextDocument):
        msg = NoScrollTextBrowser()
        msg.setDocument(document.clone())

        if type == ChatType.SENDER:
            msg.setObjectName('sender_message')
            self.layout.addWidget(msg, 0, modules.Qt.AlignRight | modules.Qt.AlignBottom)
        else:
            msg.setObjectName('other_message')
            self.layout.addWidget(msg, 0, modules.Qt.AlignLeft | modules.Qt.AlignBottom)
        
        self.num_msgs += 1
    

