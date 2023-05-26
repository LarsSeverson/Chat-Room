from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

from UI.menu import Menu
from UI.chat_ui import ChatUI
from UI.button import *

class WindowUI:
    def __init__(self, main_window):
        self.window = main_window

        size_policy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(100)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)

        self.central_widget = QWidget(main_window)
        self.central_widget.setObjectName('central_widget')
        self.central_widget.setStyleSheet('background-color: white;')

        self.horizontal_layout = QHBoxLayout(self.central_widget)
        self.horizontal_layout.setContentsMargins(0,0,0,0)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName('horizontal_layout')

        self.menu = Menu(self.central_widget)

        self.menu.set_chat_callback(self.open_chat)
        self.menu.set_profile_callback(self.open_profile)

        self.chat = ChatUI(self.central_widget)

        self.horizontal_layout.addWidget(self.menu.get_frame())
        self.horizontal_layout.addLayout(self.chat.get_layout())

        main_window.setCentralWidget(self.central_widget)
        QtCore.QMetaObject.connectSlotsByName(main_window)

        self.menu.open_chat()

    def open_chat(self):
        self.chat.open()
    
    def open_profile(self):
        self.chat.close()
    def resize_signal(self, width, height):
        self.chat.resize_signal(width, height)