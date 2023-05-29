import modules

from UI.buttons.button import *

class ChatButton(modules.QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.is_open = False
        
        self.setEnabled(True)
        self.setGeometry(0,55,51,51)
        self.setAutoFillBackground(False)
        self.setStyleSheet(ButtonStyleSheets.default)

        self.chat_icon = modules.QtGui.QIcon()
        self.chat_icon.addPixmap(modules.QtGui.QPixmap("src/UI/assets/chat.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)

        self.setIcon(self.chat_icon)
        self.setIconSize(modules.QtCore.QSize(35, 35))    

        self.setObjectName('chat_button')
    
    def open(self):
        self.setStyleSheet('''
        QPushButton{
            border-top: 10px solid white;
            border-left: 5px solid rgb(240, 240, 240);
            border-right: 5px solid rgb(240, 240, 240);
            border-bottom: 10px solid white;
        }
        ''')
        self.is_open = True

    def reset(self):
        self.setStyleSheet(ButtonStyleSheets.default)
        self.is_open = False
