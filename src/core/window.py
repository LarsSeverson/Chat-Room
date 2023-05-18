from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtGui


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.setGeometry(200,200, 1280,720)
        self.setWindowTitle('Chat-Room')
        self.setWindowIcon(QtGui.QIcon('./UI/assets/icon.png'))