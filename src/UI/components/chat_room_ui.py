from PyQt5 import QtGui
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
    
    def set_margin(self, margin: int, width: int):
        val = (width-60) - margin
        if val < 700:
            val = 700
            
        self.setStyleSheet(
            f"""
            QTextBrowser {{
                border-radius: 10px;
                margin-bottom: 10px;
                margin-left: 20px; 
                margin-right: 20px;
            }}
            
            #sender_message {{
                background-color: lightblue;
                margin-left: {val}px;
            }}
            
            #other_message {{
                background-color: white;
                margin-right: {val}px;
            }}
            """
        )


    def wheelEvent(self, e: modules.QWheelEvent) -> None:
        e.ignore()


class ChatRoom(modules.QScrollArea):
    def __init__(self, frame=None):
        super().__init__(frame)

        self.contents = modules.QWidget()

        self.layout = modules.QVBoxLayout(self.contents)

        self.setWidgetResizable(True)
        self.setWidget(self.contents)
        self.setObjectName('chat_room')

    def add_txt_msg(self, type: ChatType, document: modules.QTextDocument):
        msg = NoScrollTextBrowser()

        msg.setDocument(document.clone())

        text_size = msg.document().size().toSize()
        font_metrics = QtGui.QFontMetrics(msg.font())
        text_width = font_metrics.width(msg.toPlainText())
    
        msg.set_margin(text_width, self.width())

        msg.setFixedHeight(text_size.height() + 10)
        msg.setMaximumWidth(self.width()-25)

        
        if type == ChatType.SENDER:
            msg.setObjectName('sender_message')
        else:
            msg.setObjectName('other_message')


        self.layout.addWidget(msg)
        self.layout.setAlignment(modules.Qt.AlignBottom)

    

