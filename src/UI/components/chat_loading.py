import modules

from UI.widgets.progress_bar.chat_loading_bar import ChatLoadingBar
from src.util.connection_thread import ConnectionCheckThread

class ChatLoading(modules.QFrame):
    def __init__(self) -> None:
        super().__init__()

        self.success = False

        self.progress_bar = ChatLoadingBar()
        self.thread = ConnectionCheckThread('127.0.0.1', 1234)

        self.layout = modules.QVBoxLayout()

        self.setLayout(self.layout)

        self.setStyleSheet('''
        background-color: white;
        border-radius: 15px;
        padding: 15px;
        ''')
        self.setVisible(False)

        self.thread.start()

    def check(self, ip, port):
        self.setVisible(True)

        self.thread = ConnectionCheckThread(ip, port)
        self.thread.viability_checked.connect(self.check_connection)

        self.loading_label = modules.QLabel('Checking...')
        self.layout.addWidget(self.loading_label)
        self.layout.addWidget(self.progress_bar)

        self.thread.start()

    def check_connection(self, is_viable) -> bool:
        if is_viable:
            self.loading_label.setText('Connection is viable. Proceeeding...')
            self.success = True
        else:
            self.loading_label.setText('Connection is not viable.')
            self.success = False
        
        self.progress_bar.setRange(0,1)
        self.progress_bar.setValue(1)