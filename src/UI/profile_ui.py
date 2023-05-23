from PyQt5 import QtWidgets, QtCore, QtGui
from UI.button import *

class ProfileButton(QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.type = Type.PROFILE
        
        self.setEnabled(True)
        self.setGeometry(0,130,61,61)
        self.setAutoFillBackground(False)
        self.setStyleSheet(ButtonStyleSheets.default)

        self.profile_icon = QtGui.QIcon()
        self.profile_icon.addPixmap(QtGui.QPixmap("src/UI/assets/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setIcon(self.profile_icon)
        self.setIconSize(QtCore.QSize(35, 55))    

        self.setObjectName('profile_button')
    
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