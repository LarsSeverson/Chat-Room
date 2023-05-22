from PyQt5 import QtCore, QtGui, QtWidgets
from UI.menu_button import MenuButton

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

        self.chat_button = QtWidgets.QPushButton(window.central_widget)
        self.set_chat_button()
        self.profile_button = QtWidgets.QPushButton(window.central_widget)
        self.set_profile_button()

        self.init_animations()

    # def open_button(self, button):
    #     self.reset_buttons(button)

    # def reset_buttons(self, no_change):
    #     for button in self.menu_buttons:
    #         if button.type != no_change:
    #             button.reset()

    def init_animations(self):
        self.left_anim = QtCore.QPropertyAnimation(self.left_frame, b'geometry')
        self.line_anim = QtCore.QPropertyAnimation(self.menu_line, b'geometry')
        self.menu_anim = QtCore.QPropertyAnimation(self.menu_button, b'geometry')
        self.left_anim.setDuration(150)
        self.menu_anim.setDuration(150)
        self.line_anim.setDuration(150)

    def set_chat_button(self):
        self.chat_button.setEnabled(True)
        self.chat_button.setGeometry(QtCore.QRect(0,60,61,61))
        self.chat_button.setAutoFillBackground(False)
        self.chat_button.setStyleSheet('''
        QPushButton{
            border:none;
        }
        QPushButton:hover{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')

        self.chat_icon = QtGui.QIcon()
        self.chat_icon.addPixmap(QtGui.QPixmap("src/UI/assets/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.chat_button.setIcon(self.chat_icon)
        self.chat_button.setIconSize(QtCore.QSize(35, 55))

        self.chat_button.clicked.connect(self.chat_open)

        self.chat_button.setObjectName('chat_button')
        
    def set_profile_button(self):
        self.profile_button.setEnabled(True)
        self.profile_button.setGeometry(QtCore.QRect(0,130,61,61))
        self.profile_button.setAutoFillBackground(False)
        self.profile_button.setStyleSheet('''
        QPushButton{
            border:none;
        }
        QPushButton:hover{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')

        self.profile_icon = QtGui.QIcon()
        self.profile_icon.addPixmap(QtGui.QPixmap("src/UI/assets/profile.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.profile_button.setIcon(self.profile_icon)
        self.profile_button.setIconSize(QtCore.QSize(35, 55))

        self.profile_button.clicked.connect(self.profile_open)

        self.profile_button.setObjectName('profile_button')
    
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
    def chat_open(self):
        self.chat_button.setStyleSheet('''
        QPushButton{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')
    def profile_open(self):
        self.profile_button.setStyleSheet('''
        QPushButton{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')        