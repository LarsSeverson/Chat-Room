from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit
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
    def __init__(self, central_widget) -> None:

        self.chat_open = False

        self.chat_box = QLineEdit(central_widget)
        self.chat_box.setGeometry(70,530,911,51)
        self.chat_box.setObjectName('chat_box')
        self.chat_box.setStyleSheet('border-radius: 15px')

        self.chat_box.setVisible(False)

    def open(self):
        self.chat_open = True
        self.chat_box.setVisible(True)
