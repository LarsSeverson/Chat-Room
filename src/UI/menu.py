from PyQt5 import QtCore, QtGui, QtWidgets

class Menu:
    def __init__(self, window) -> None:

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
    
        # start menu_button
        self.menu_button = QtWidgets.QPushButton(window.central_widget)
        self.menu_button.setEnabled(True)
        self.menu_button.setGeometry(QtCore.QRect(10,10,41,41))
        self.menu_button.setAutoFillBackground(False)
        self.menu_button.setStyleSheet('border: none;')
        
        self.menu_icon = QtGui.QIcon()
        self.menu_icon_open = QtGui.QIcon()
        self.menu_icon.addPixmap(QtGui.QPixmap("src/UI/assets/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menu_icon_open.addPixmap(QtGui.QPixmap("src/UI/assets/menu_icon_open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menu_button.setIcon(self.menu_icon)
        self.menu_button.setIconSize(QtCore.QSize(35, 55))
        self.menu_button.enterEvent = self.menu_hover
        self.menu_button.leaveEvent = self.menu_unhover
        self.menu_button.clicked.connect(self.menu_open)
        self.menu_button.setObjectName('menu_button')
        # end menu_button

        self.init_animations()

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

        self.menu_button.setIcon(self.menu_icon_open)        

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

        self.menu_button.setIcon(self.menu_icon)

        self.left_anim.start()
        self.line_anim.start()
        self.menu_anim.start()

        self.menu_is_open = False
    def menu_hover(self, event):
        self.menu_button.setIconSize(QtCore.QSize(40, 60))
    def menu_unhover(self, event):
        self.menu_button.setIconSize(QtCore.QSize(35, 55))