from PyQt5 import QtWidgets, QtCore, QtGui
from UI.button import *

class ChatButton(QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.type = Type.CHAT
        
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

    def reset(self):
        self.setStyleSheet(ButtonStyleSheets.default)