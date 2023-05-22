from PyQt5 import QtCore, QtGui, QtWidgets
from UI.menu import Menu

class WindowUI:
    def __init__(self, main_window) -> None:
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')
        main_window.setCentralWidget(self.central_widget)

        self.width = main_window.width
        self.height = main_window.height

        self.menu = Menu(self)

        # self.menu_bar = QtWidgets.QMenuBar(main_window)
        # self.menu_bar.setGeometry(QtCore.QRect(0,0,992,21))
        # self.menu_bar.setObjectName('menu_bar')
        # main_window.setMenuBar(self.menu_bar)

        # self.status_bar = QtWidgets.QStatusBar(main_window)
        # self.status_bar.setObjectName('status_bar')
        # main_window.setStatusBar(self.status_bar)

        QtCore.QMetaObject.connectSlotsByName(main_window)