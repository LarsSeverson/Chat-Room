import modules
from UI.components.chat_room_ui import ChatRoom
from src.core.chat import ChatType

class ChatBox(modules.QTextEdit):
    def __init__(self, frame):
        super().__init__(frame)

        self.font = modules.QFont()
        self.font.setFamily('Comic Sans MS')
        self.font.setPointSize(11)
        self.setFont(self.font)

        self.scrollbar = self.verticalScrollBar()
        self.scrollbar.setStyleSheet('width: 0px;')
        self.scrollbar.setVisible(False)

        self.setStyleSheet('''     
        border-radius: 15px;
        background-color: white;
        padding-top: 2px;
        padding-left: 10px;
        padding-right: 10px;
        ''')

        self.setPlaceholderText('Type message')
        self.setMaximumHeight(35)
        self.setObjectName('chat_box')

        self.send_button = modules.QPushButton(self)
        self.send_button.setGeometry(1170, 5, 27, 25)
        self.send_button.setObjectName('sender_bud')

        self.send_icon = modules.QtGui.QIcon()
        self.send_idle_icon = modules.QtGui.QIcon()
        self.send_icon.addPixmap(modules.QtGui.QPixmap("src/UI/assets/send.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)
        self.send_idle_icon.addPixmap(modules.QtGui.QPixmap("src/UI/assets/send_idle.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)
        
        self.send_button.setIcon(self.send_idle_icon)
        self.send_button.setIconSize(modules.QtCore.QSize(25, 25))     
        
        self.send_button.clicked.connect(self.send_message)    
        self.textChanged.connect(self.text)
 
    def keyPressEvent(self, e: modules.QKeyEvent) -> None:
        if e.key() == modules.Qt.Key.Key_Return or e.key() == modules.Qt.Key_Enter:
            if e.modifiers() == modules.Qt.ShiftModifier:
                return super().keyPressEvent(e)
            
            self.send_message()
            return
        return super().keyPressEvent(e)
    
    def send_message(self):
        if len(self.toPlainText()):
            self.send_callback(self.document())

            self.clear()

    def text(self):
        self.handle_height()

        if len(self.toPlainText()) == 0:
            self.send_button.setIcon(self.send_idle_icon)
            self.send_button.setStyleSheet('''
            QPushButton#sender_button {
                background-color: transparent;
                border: none;
            }
            ''')
        else:
            self.send_button.setIcon(self.send_icon)
            self.send_button.setStyleSheet('''
            QPushButton#sender_button {
                background-color: transparent;
                border: none;
            }
            QPushButton#senderbud:hover{
                border-radius: 12px;
                background-color: rgb(229, 229, 229);
            }
            ''')  
    def set_send_callback(self, func):
        self.send_callback = func

    def handle_height(self):
        height = int(self.document().size().height())
        if height < 28:
            self.setMaximumHeight(35)
        else:
            self.setMaximumHeight(height + 7)

    def resize(self, width, height):
        self.send_button.setGeometry(width-110, 5, 27, 25)

class ChatUI():
    def __init__(self, central_widget) -> None:

        self.chat_open = False

        self.layout = modules.QVBoxLayout()
        self.layout.setObjectName('chat_layout')
        
        self.chat_frame = modules.QFrame(central_widget)
        self.chat_frame.setFrameShape(modules.QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(modules.QFrame.Raised)
        self.chat_frame.setStyleSheet('background-color: rgb(240, 240, 240);')

        self.chat_layout = modules.QVBoxLayout(self.chat_frame)
        self.chat_layout.setObjectName('chat_layout')

        self.layout.addWidget(self.chat_frame)

        self.chat_room = ChatRoom(self.chat_frame)

        self.chat_box = ChatBox(self.chat_frame)
        self.chat_box.set_send_callback(self.send_txt_msg)

        self.chat_layout.addWidget(self.chat_room, 0)
        self.chat_layout.addWidget(self.chat_box, 0, modules.Qt.AlignBottom)

    def resize_signal(self, width, height):
        self.chat_box.handle_height()
        self.chat_box.resize(width, height)

    def send_txt_msg(self, text: str):
        self.chat_room.add_txt_msg(ChatType.SENDER, text)

    def get_layout(self):
        return self.layout

    def open(self):
        self.chat_open = True
        self.chat_frame.setVisible(True)

    def close(self):
        self.chat_open = False
        self.chat_frame.setVisible(False)
