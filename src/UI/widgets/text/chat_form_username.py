import modules

import src.util.checker as check

class FormUsername(modules.QLineEdit):
    def __init__(self):
        super().__init__()

        self.check = False

        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(15)

        self.setFont(self.font)
        self.setPlaceholderText('Username') 
        self.setSizePolicy(modules.QSizePolicy.Preferred, modules.QSizePolicy.Preferred)  
        self.setStyleSheet('''
        border-radius: 15px;
        border: 2px solid rgb(255, 192, 192);
        background-color: rgb(210, 210, 210);
        ''')   
        self.textChanged.connect(self.handle_text)

    def handle_text(self, text):
        if check.check_user(text):
            self.setStyleSheet('''
            border-radius: 15px;           
            border: 2px solid rgb(160, 200, 160);
            background-color: rgb(210, 210, 210);
            ''')
            self.check = True
        else:
            self.setStyleSheet('''
            border-radius: 15px;
            border: 2px solid rgb(255, 192, 192);
            background-color: rgb(210, 210, 210);
            ''')  
