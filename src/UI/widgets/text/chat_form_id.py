import modules

class FormID(modules.QLineEdit):
    def __init__(self):
        super().__init__()

        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(12)     

        self.setFont(self.font)
        self.setMinimumHeight(55)
        self.setMaximumWidth(70)
        self.setPlaceholderText('ID')
        self.setSizePolicy(modules.QSizePolicy.Ignored, modules.QSizePolicy.Ignored)
        self.setStyleSheet('''
        border-radius: 15px;
        background-color: rgb(210, 210, 210);
        ''')

        self.setMaxLength(4)