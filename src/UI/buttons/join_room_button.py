import modules

class JoinRoomButton(modules.QPushButton):
    def __init__(self):
        super().__init__()

        self.setStyleSheet('''
        QPushButton
        {
        background-color: rgb(227, 227, 227);
        }
        QPushButton:hover
        {
        background-color: rgb(210, 210, 210);
        }
        ''')

    def open(self):
        self.setStyleSheet('''
        QPushButton{
        background-color: rgb(210, 210, 210);
        border-bottom: 5px solid lightblue;
        }
        
        ''')
    def close(self):
        self.setStyleSheet('''
        QPushButton
        {
        background-color: rgb(227, 227, 227);
        }
        QPushButton:hover
        {
        background-color: rgb(210, 210, 210);
        }
        ''')