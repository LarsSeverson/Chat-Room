from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from UI.menu import Menu
from UI.chat_ui import ChatUI
from UI.button import *

class WindowUI:
    def __init__(self, main_window):
        self.window = main_window
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')

        self.horizontal_layout = QHBoxLayout(self.central_widget)
        self.horizontal_layout.setObjectName('horizontal_layout')

        main_window.setCentralWidget(self.central_widget)

        self.width = main_window.width()
        self.height = main_window.height()

        self.menu = Menu(self.central_widget, self.width, self.height)
        self.menu.set_chat_callback(self.open_chat)
        self.menu.set_profile_callback(self.open_profile)

        self.chat = ChatUI(self)

        # self.menu_bar = QtWidgets.QMenuBar(main_window)
        # self.menu_bar.setGeometry(QtCore.QRect(0,0,992,21))
        # self.menu_bar.setObjectName('menu_bar')
        # main_window.setMenuBar(self.menu_bar)

        # self.status_bar = QtWidgets.QStatusBar(main_window)
        # self.status_bar.setObjectName('status_bar')
        # main_window.setStatusBar(self.status_bar)

        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.menu.open_chat()

    def open_chat(self):
        self.chat.open()
    
    def open_profile(self):
        self.chat.close()
    def get_line_seperator(self):
        return self.menu.line_x