from core.window import Window
from PyQt5.QtWidgets import QApplication
import sys

class Application:
    def __init__(self) -> None:
        self.app = QApplication(sys.argv)
        self.window = Window()    
    def run(self):
        self.window.show()
        sys.exit(self.app.exec_())
