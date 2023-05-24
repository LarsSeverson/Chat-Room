from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.button import *

class ChatButton(QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.type = Type.CHAT
        self.is_open = False
        
        self.setEnabled(True)
        self.setGeometry(0,60,61,61)
        self.setAutoFillBackground(False)
        self.setStyleSheet(ButtonStyleSheets.default)

        self.chat_icon = QtGui.QIcon()
        self.chat_icon.addPixmap(QtGui.QPixmap("src/UI/assets/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setIcon(self.chat_icon)
        self.setIconSize(QtCore.QSize(35, 55))    

        self.setObjectName('chat_button')
    
    def open(self):
        self.setStyleSheet('''
        QPushButton{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')
        self.is_open = True

    def reset(self):
        self.setStyleSheet(ButtonStyleSheets.default)
        self.is_open = False

class ChatBox(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent.chat_frame)
        self.font = QFont()
        self.font.setFamily('Comic Sans MS')
        self.font.setPointSize(11)

        self.p_height = parent.height

        self.setGeometry(parent.x-50, parent.height - 50, parent.width-20,35)
        self.setStyleSheet('''     
        border-radius: 15px;
        background-color: white;
        padding-top: 2px;
        padding-left: 10px;
        padding-right: 10px;
        ''')

        self.setPlaceholderText('Type message')
        self.setFont(self.font)
        self.setObjectName('chat_box')
        self.textChanged.connect(self.handle_height)

        self.last_height = 35

        self.scrollbar = self.verticalScrollBar()
        self.scrollbar.setStyleSheet('width: 0px;')
        self.scrollbar.setVisible(False)

    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key_Enter:
            return
        return super().keyPressEvent(e)

    def handle_height(self):
        curr_height = self.height()
        height = int(self.document().size().height())
        if height > 35:

            self.setFixedHeight(height)
            if height < self.last_height:
                self.move(self.x(), self.y() + (curr_height - height))    
            else:
                self.move(self.x(), self.y() - (height - curr_height))
            self.last_height = height

        else:
            self.setFixedHeight(35) 
            self.move(self.x(), self.p_height - 50)

class ChatUI():
    def __init__(self, main_window) -> None:

        self.chat_open = False

        self.x = main_window.get_line_seperator()
        self.y = 0
        self.width = main_window.width - main_window.get_line_seperator()
        self.height = main_window.height

        self.chat_frame = QFrame(main_window.central_widget)
        self.chat_frame.setGeometry(self.x, self.y, self.width, self.height)

        self.chat_frame.setVisible(False)

        self.chat_box = ChatBox(self)

    def open(self):
        self.chat_open = True
        self.chat_frame.setVisible(True)

    def close(self):
        self.chat_open = False
        self.chat_frame.setVisible(False)
