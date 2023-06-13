import modules

import src.util.checker as check

class FormID(modules.QLineEdit):
    def __init__(self):
        super().__init__()

        self.match = True

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
        border: 2px solid rgb(255, 192, 192);
        ''')

        self.setMaxLength(4)
        self.textChanged.connect(self.handle_text)

    def handle_text(self, text):
        if check.check_id(text):
            self.setStyleSheet('''
            border-radius: 15px;
            background-color: rgb(210, 210, 210);
            border: 2px solid rgb(160, 200, 160);
            ''')
            self.match = True
        else:
            self.setStyleSheet('''
            border-radius: 15px;
            border: 2px solid rgb(255, 192, 192);
            background-color: rgb(210, 210, 210);
            ''')