from PyQt5 import QtCore, QtGui, QtWidgets

class WindowUI:
    def __init__(self, main_window) -> None:
        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName('central_widget')
        main_window.setCentralWidget(self.central_widget)

        self.menu(main_window)

        # self.menu_bar = QtWidgets.QMenuBar(main_window)
        # self.menu_bar.setGeometry(QtCore.QRect(0,0,992,21))
        # self.menu_bar.setObjectName('menu_bar')
        # main_window.setMenuBar(self.menu_bar)

        # self.status_bar = QtWidgets.QStatusBar(main_window)
        # self.status_bar.setObjectName('status_bar')
        # main_window.setStatusBar(self.status_bar)

        QtCore.QMetaObject.connectSlotsByName(main_window)
        
    def menu(self, main_window):
        # start menu_line:
        self.menu_line = QtWidgets.QFrame(self.central_widget)        
        self.menu_line.setGeometry(QtCore.QRect(50,0,20,main_window.height))
        self.menu_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.menu_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.menu_line.setObjectName('menu_line')        
        # end menu_line
        
        # start menu_button
        self.menu_button = QtWidgets.QPushButton(self.central_widget)
        self.menu_button.setEnabled(True)
        self.menu_button.setGeometry(QtCore.QRect(10,10,41,41))
        self.menu_button.setAutoFillBackground(False)
        self.menu_button.setStyleSheet('border: none')
        self.menu_button.setText('')
        
        self.menu_icon = QtGui.QIcon()
        self.menu_icon.addPixmap(QtGui.QPixmap("UI/assets/menu_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.menu_button.setIcon(self.menu_icon)
        self.menu_button.setIconSize(QtCore.QSize(35, 55))
        self.menu_button.setObjectName('menu_button')
        # end menu_button