from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QFontMetricsF
from PyQt5.QtCore import Qt
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

class ChatUI:
    def __init__(self, main_window) -> None:

        self.chat_open = False
        
        self.font = QFont()
        self.font.setFamily('Comic Sans MS')
        self.font.setPointSize(11)

        self.x = main_window.get_line_seperator()
        self.y = 0
        self.width = main_window.width - main_window.get_line_seperator()
        self.height = main_window.height

        self.chat_frame = QFrame(main_window.central_widget)
        self.chat_frame.setGeometry(self.x, self.y, self.width, self.height)

        self.chat_box = QTextEdit(self.chat_frame)
        self.chat_box.setGeometry(self.x-50, self.height - 50, self.width-20,35)
        self.chat_box.setStyleSheet('''     
        border-radius: 15px;
        background-color: white;
        padding-top: 2px;
        padding-left: 10px;
        padding-right: 10px;
        ''')
        self.chat_box.setPlaceholderText('Type message')
        self.chat_box.setFont(self.font)
        self.chat_box.setObjectName('chat_box')
        self.chat_box.textChanged.connect(self.handle_height)

        self.last_height = 35

        self.scrollbar = self.chat_box.verticalScrollBar()
        self.scrollbar.setVisible(False)
        
        self.chat_frame.setVisible(False)

    def open(self):
        self.chat_open = True
        self.chat_frame.setVisible(True)

    def close(self):
        self.chat_open = False
        self.chat_frame.setVisible(False)

    def handle_height(self):
        curr_height = self.chat_box.height()
        height = int(self.chat_box.document().size().height())
        if height > 35:

            self.chat_box.setFixedHeight(height)
            if height < self.last_height:
                self.chat_box.move(self.chat_box.x(), self.chat_box.y() + (curr_height - height))    
            else:
                self.chat_box.move(self.chat_box.x(), self.chat_box.y() - (height - curr_height))
            self.last_height = height
            
        else:
            self.chat_box.setFixedHeight(35) 
            self.chat_box.move(self.chat_box.x(), self.height - 50)
