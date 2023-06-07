import modules

class ExecuteJoinRoomButton(modules.QPushButton):
    def __init__(self):
        super().__init__()

        self.icon = modules.QIcon()
        self.icon.addPixmap(modules.QtGui.QPixmap("src/UI/assets/join.png"), modules.QtGui.QIcon.Normal, modules.QtGui.QIcon.Off)

        self.setSizePolicy(modules.QSizePolicy.Minimum, modules.QSizePolicy.Preferred)
        self.setStyleSheet('''
        QPushButton
        {
            border-radius: 20px;
            background-color: rgb(176, 224, 230);
        }
        QPushButton:hover
        {
            background-color: rgb(166, 214, 220);
        }
        ''')
        self.setCursor(modules.QCursor(modules.Qt.PointingHandCursor))

        self.setIconSize(modules.QSize(50,50))
        self.setIcon(self.icon)

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

        self.setCursor(modules.QCursor(modules.Qt.PointingHandCursor))

    def open(self):
        self.setStyleSheet('''
        QPushButton{
        background-color: rgb(210, 210, 210);
        border-bottom: 5px solid rgb(176, 224, 230);
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