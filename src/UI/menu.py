from PyQt5 import QtCore, QtGui, QtWidgets
from UI.menu_button import MenuButton
from UI.chat_ui import ChatButton
from UI.profile_ui import ProfileButton

class Menu:
    def __init__(self, window) -> None:
        self.menu_buttons = []
        self.menu_is_open = False
        self.line_x = 60
        self.w_width = window.width
        self.w_height = window.height

        self.left_frame = QtWidgets.QFrame(window.central_widget)
        self.left_frame.setGeometry(QtCore.QRect(0,0, self.line_x, window.height))
        self.left_frame.setStyleSheet("background-color: white;")

        self.menu_line = QtWidgets.QFrame(window.central_widget)        
        self.menu_line.setGeometry(QtCore.QRect(self.line_x, 0, 2, window.height))
        self.menu_line.setLineWidth(22)
        self.menu_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menu_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menu_line.setObjectName('menu_line')
        self.menu_line.setStyleSheet('border: none; background-color: rgb(229, 229, 229);')  
    
        self.menu_button = MenuButton(window.central_widget)
        self.menu_button.clicked.connect(self.menu_open)
        self.menu_buttons.append(self.menu_button)

        self.chat_button = ChatButton(window.central_widget)
        self.chat_button.clicked.connect(self.open_chat)
        self.menu_buttons.append(self.chat_button)

        self.profile_button = ProfileButton(window.central_widget)
        self.profile_button.clicked.connect(self.open_profile)
        self.menu_buttons.append(self.profile_button) 
       
        self.init_animations()


    def open_chat(self):
        for button in self.menu_buttons:
            if button.type != self.chat_button.type:
                button.reset()
        if not self.chat_button.is_open:
            self.chat_button.open()
            self.chat_callback()

    def open_profile(self):
        for button in self.menu_buttons:
            if button.type != self.profile_button.type:
                button.reset()
        if not self.profile_button.is_open:
            self.profile_button.open()
            self.profile_callback()

    def init_animations(self):
        self.left_anim = QtCore.QPropertyAnimation(self.left_frame, b'geometry')
        self.line_anim = QtCore.QPropertyAnimation(self.menu_line, b'geometry')
        self.menu_anim = QtCore.QPropertyAnimation(self.menu_button, b'geometry')
        self.left_anim.setDuration(150)
        self.menu_anim.setDuration(150)
        self.line_anim.setDuration(150)
        
    
    def menu_open(self):
        if self.menu_is_open:
            self.menu_close()
            return
        
        self.left_anim.setStartValue(QtCore.QRect(0,0, self.line_x, self.w_height))
        self.line_anim.setStartValue(QtCore.QRect(60,0, 2, self.w_height))
        self.menu_anim.setStartValue(QtCore.QRect(10, 10, 41,41))
        self.line_x = 150
        self.line_anim.setEndValue(QtCore.QRect(self.line_x, 0, 2, self.w_height))
        self.menu_anim.setEndValue(QtCore.QRect(110, 10, 41,41))
        self.left_anim.setEndValue(QtCore.QRect(0,0, self.line_x, self.w_height)) 

        self.menu_button.setIcon(self.menu_button.menu_icon_open)        

        self.left_anim.start()
        self.line_anim.start()
        self.menu_anim.start()

        self.menu_is_open = True
        
    def menu_close(self):
        self.left_anim.setStartValue(QtCore.QRect(0,0, self.line_x, self.w_height))
        self.line_anim.setStartValue(QtCore.QRect(self.line_x, 0, 2, self.w_height))
        self.menu_anim.setStartValue(QtCore.QRect(110, 10, 41,41))
        self.line_x = 60
        self.line_anim.setEndValue(QtCore.QRect(self.line_x, 0, 2, self.w_height))
        self.menu_anim.setEndValue(QtCore.QRect(10, 10, 41,41))
        self.left_anim.setEndValue(QtCore.QRect(0,0, self.line_x, self.w_height))

        self.menu_button.setIcon(self.menu_button.menu_icon)

        self.left_anim.start()
        self.line_anim.start()
        self.menu_anim.start()

        self.menu_is_open = False 
    
    def set_chat_callback(self, func):
        self.chat_callback = func
    def set_profile_callback(self, func):
        self.profile_callback = func