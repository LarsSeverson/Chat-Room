import modules

from UI.buttons.menu_button import MenuButton
from UI.buttons.chat_button import ChatButton
from UI.buttons.profile_button import ProfileButton

class Menu:
    def __init__(self, central_widget) -> None:
        self.menu_buttons = []
        self.menu_is_open = False

        self.left_frame = modules.QtWidgets.QFrame(central_widget)
        self.left_frame.setMinimumSize(51, 0)
        self.left_frame.setMaximumSize(35, 16777215)
        self.left_frame.setFrameShape(modules.QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(modules.QtWidgets.QFrame.Raised)
        self.left_frame.setStyleSheet("background-color: white;")

        self.menu_button = MenuButton(central_widget)
        self.menu_button.clicked.connect(self.menu_open)
        self.menu_buttons.append(self.menu_button)

        self.chat_button = ChatButton(central_widget)
        self.chat_button.clicked.connect(self.open_chat)
        self.menu_buttons.append(self.chat_button)

        self.profile_button = ProfileButton(central_widget)
        self.profile_button.clicked.connect(self.open_profile)
        self.menu_buttons.append(self.profile_button) 
       
        self.init_animations()


    def open_chat(self):
        for button in self.menu_buttons:
            if button != self.chat_button:
                button.reset()
        if not self.chat_button.is_open:
            self.chat_button.open()
            self.chat_callback()

    def open_profile(self):
        for button in self.menu_buttons:
            if button != self.profile_button:
                button.reset()
        if not self.profile_button.is_open:
            self.profile_button.open()
            self.profile_callback()

    def init_animations(self):
        self.left_anim = modules.QtCore.QPropertyAnimation(self.left_frame, b'minimumWidth')
        self.menu_anim = modules.QtCore.QPropertyAnimation(self.menu_button, b'pos')
        self.left_anim.setDuration(150)
        self.menu_anim.setDuration(150)
        
    
    def menu_open(self):
        if self.menu_is_open:
            self.menu_close()
            return
        
        self.left_anim.setStartValue(self.left_frame.minimumWidth())
        self.left_anim.setEndValue(100)

        self.menu_anim.setStartValue(self.menu_button.pos())
        self.menu_anim.setEndValue(modules.QtCore.QPoint(50, self.menu_button.y()))
        
        self.menu_button.setIcon(self.menu_button.menu_icon_open)        
        
        self.left_anim.start()
        self.menu_anim.start()

        self.menu_is_open = True
        
    def menu_close(self):

        self.left_anim.setStartValue(self.left_frame.minimumWidth())
        self.left_anim.setEndValue(51)

        self.menu_anim.setStartValue(self.menu_button.pos())
        self.menu_anim.setEndValue(modules.QtCore.QPoint(0, self.menu_button.y()))
       
        self.menu_button.setIcon(self.menu_button.menu_icon)

        self.left_anim.start()
        self.menu_anim.start()

        self.menu_is_open = False 

    def get_frame(self):
        return self.left_frame
    
    def set_chat_callback(self, func):
        self.chat_callback = func
    def set_profile_callback(self, func):
        self.profile_callback = func
    def set_menu_open_signal(self, func):
        self.open_signal = func