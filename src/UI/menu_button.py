from PyQt5 import QtWidgets, QtCore, QtGui
from UI.button import *

class MenuButton(QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.type = Type.MENU
        
        self.setEnabled(True)
        self.setGeometry(0,0,51,51)
        self.setAutoFillBackground(False)
        self.setStyleSheet('border: none')

        self.menu_icon = QtGui.QIcon()
        self.menu_icon_open = QtGui.QIcon()
        self.menu_icon.addPixmap(QtGui.QPixmap("src/UI/assets/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_icon_open.addPixmap(QtGui.QPixmap("src/UI/assets/menu_icon_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setIcon(self.menu_icon)
        self.setIconSize(QtCore.QSize(35, 35))    

        self.enterEvent = self.menu_hover
        self.leaveEvent = self.menu_unhover

        self.setObjectName('menu_button')


    def menu_hover(self, event):
        self.setIconSize(QtCore.QSize(40, 60))
    def menu_unhover(self, event):
        self.setIconSize(QtCore.QSize(35, 55))

    def reset(self):
        ...
