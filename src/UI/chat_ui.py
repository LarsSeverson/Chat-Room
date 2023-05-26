from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI.button import *

class ChatButton(QtWidgets.QPushButton):
    def __init__(self, central_widget=None) -> None:
        super().__init__(central_widget)

        self.type = Type.CHAT
        self.is_open = False
        
        self.setEnabled(True)
        self.setGeometry(0,55,51,51)
        self.setAutoFillBackground(False)
        self.setStyleSheet(ButtonStyleSheets.default)

        self.chat_icon = QtGui.QIcon()
        self.chat_icon.addPixmap(QtGui.QPixmap("src/UI/assets/chat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.setIcon(self.chat_icon)
        self.setIconSize(QtCore.QSize(35, 35))    

        self.setObjectName('chat_button')
    
    def open(self):
        self.setStyleSheet('''
        QPushButton{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }
        ''')
        self.is_open = True

    def reset(self):
        self.setStyleSheet(ButtonStyleSheets.default)
        self.is_open = False

class ChatBox(QTextEdit):
    def __init__(self, parent):
        super().__init__(parent.chat_frame)

        self.font = QFont()
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

        self.send_button = QPushButton(self)
        self.send_button.setGeometry(1170, 5, 27, 25)
        self.send_button.setObjectName('senderbud')

        self.send_icon = QtGui.QIcon()
        self.send_idle_icon = QtGui.QIcon()
        self.send_icon.addPixmap(QtGui.QPixmap("src/UI/assets/send.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_idle_icon.addPixmap(QtGui.QPixmap("src/UI/assets/send_idle.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        
        self.send_button.setIcon(self.send_idle_icon)
        self.send_button.setIconSize(QtCore.QSize(25, 25))     
        
        self.send_button.clicked.connect(self.send_message)    
        self.textChanged.connect(self.text)
 
    def keyPressEvent(self, e: QKeyEvent) -> None:
        if e.key() == Qt.Key.Key_Return or e.key() == Qt.Key_Enter:
            return
        return super().keyPressEvent(e)
    
    def send_message(self):
        if len(self.toPlainText()):
            print('msg')

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

        self.layout = QVBoxLayout()
        self.layout.setObjectName('chat_layout')
        
        self.chat_frame = QFrame(central_widget)
        self.chat_frame.setFrameShape(QFrame.StyledPanel)
        self.chat_frame.setFrameShadow(QFrame.Raised)
        self.chat_frame.setStyleSheet('background-color: rgb(240, 240, 240);')

        self.chat_layout = QVBoxLayout(self.chat_frame)
        self.chat_layout.setObjectName('chat_layout')

        self.layout.addWidget(self.chat_frame)

        self.chat_box = ChatBox(self)
        self.chat_layout.addWidget(self.chat_box, 0, Qt.AlignBottom)

    def resize_signal(self, width, height):
        self.chat_box.handle_height()
        self.chat_box.resize(width, height)

    def get_layout(self):
        return self.layout

    def open(self):
        self.chat_open = True
        self.chat_frame.setVisible(True)

    def close(self):
        self.chat_open = False
        self.chat_frame.setVisible(False)
