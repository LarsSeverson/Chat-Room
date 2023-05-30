import modules

from UI.frames.menu import Menu
from UI.frames.chat_ui import ChatUI
from UI.buttons.button import *

class WindowUI:
    def __init__(self, main_window):
        self.window = main_window

        size_policy = modules.QtWidgets.QSizePolicy(modules.QtWidgets.QSizePolicy.Fixed, modules.QtWidgets.QSizePolicy.Preferred)
        size_policy.setHorizontalStretch(100)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(main_window.sizePolicy().hasHeightForWidth())
        main_window.setSizePolicy(size_policy)

        self.central_widget = modules.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')
        self.central_widget.setStyleSheet('background-color: white;')

        self.horizontal_layout = modules.QHBoxLayout(self.central_widget)
        self.horizontal_layout.setContentsMargins(0,0,0,0)
        self.horizontal_layout.setSpacing(0)
        self.horizontal_layout.setObjectName('horizontal_layout')

        self.menu = Menu(self.central_widget)

        self.menu.set_chat_callback(self.open_chat)
        self.menu.set_profile_callback(self.open_profile)
        self.menu.set_menu_open_signal(self.resize_signal)

        self.chat = ChatUI(self.central_widget)

        self.horizontal_layout.addWidget(self.menu.get_frame())
        self.horizontal_layout.addLayout(self.chat.get_layout())

        main_window.setCentralWidget(self.central_widget)
        modules.QtCore.QMetaObject.connectSlotsByName(main_window)

        self.menu.open_chat()

    def open_chat(self):
        self.chat.open()
    
    def open_profile(self):
        self.chat.close()
    def resize_signal(self, width, height):
        self.chat.resize_signal(width, height)
    
    def set_text_callback(self, func):
        self.chat.set_text_callback(func)
    