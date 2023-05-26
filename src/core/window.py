from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QBrush

from UI.window_ui import WindowUI


class Window(QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.setGeometry(200,200, 1280,720)
        self.setWindowTitle('Chat-Room')
        self.setWindowIcon(QtGui.QIcon('src/UI/assets/icon.png'))
        self.setAnimated(True)

        self.setup_ui()
        

    def setup_ui(self):
        print(self.width)
        self.ui = WindowUI(self)
    
    def button_event(self, type):
        pass
    
    def resizeEvent(self, event) -> None:
        self.ui.resize_signal(self.width(), self.height())
        return super().resizeEvent(event)
