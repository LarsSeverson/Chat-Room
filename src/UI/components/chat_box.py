import modules
class ChatBox(modules.QTextEdit):
    def __init__(self):
        super().__init__()

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

        self.setVisible(True)
 
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
            QPushButton#sender_bud {
                background-color: transparent;
                border: none;
            }
            ''')
        else:
            self.send_button.setIcon(self.send_icon)
            self.send_button.setStyleSheet('''
            QPushButton#sender_bud {
                background-color: transparent;
                border: none;
            }
            QPushButton#sender_bud:hover{
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
        self.send_button.setGeometry(width-60, 5, 27, 25)
