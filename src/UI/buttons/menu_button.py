import modules

from UI.buttons.button import *

class MenuButton(modules.QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.setEnabled(True)
        self.setGeometry(0,0,51,51)
        self.setAutoFillBackground(False)
        self.setStyleSheet('border: none')

        self.menu_icon = modules.QtGui.QIcon()
        self.menu_icon_open = modules.QtGui.QIcon()
        self.menu_icon.addPixmap(modules.QtGui.QPixmap("src/UI/assets/menu_icon.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)
        self.menu_icon_open.addPixmap(modules.QtGui.QPixmap("src/UI/assets/menu_icon_open.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)

        self.setCursor(modules.QCursor(modules.Qt.PointingHandCursor))

        self.setIcon(self.menu_icon)
        self.setIconSize(modules.QtCore.QSize(35, 35))    

        self.enterEvent = self.menu_hover
        self.leaveEvent = self.menu_unhover

        self.setObjectName('menu_button')


    def menu_hover(self, event):
        self.setIconSize(modules.QtCore.QSize(40, 60))
    def menu_unhover(self, event):
        self.setIconSize(modules.QtCore.QSize(35, 55))

    def reset(self):
        ...
