import modules

from UI.window_ui import WindowUI

from src.core.chat import Chat


class Window(modules.QMainWindow):
    def __init__(self) -> None:
        super(Window, self).__init__()
        self.setGeometry(200,200, 1280,720)
        self.setWindowTitle('Chat-Room')
        self.setWindowIcon(modules.QtGui.QIcon('src/UI/assets/icon.png'))
        self.setAnimated(True)

        self.init_ui()

    def init_ui(self):
        self.ui = WindowUI(self)

    def set_text_callback(self, func):
        self.ui.set_text_callback(func)
    
    def resizeEvent(self, event) -> None:
        self.ui.resize_signal(self.width(), self.height())
        return super().resizeEvent(event)
