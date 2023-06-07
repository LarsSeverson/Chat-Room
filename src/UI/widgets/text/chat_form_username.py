import modules

class FormUsername(modules.QLineEdit):
    def __init__(self):
        super().__init__()

        self.font = modules.QFont()
        self.font.setFamily('Franklin Gothic Small')
        self.font.setPointSize(15)

        self.setFont(self.font)
        self.setPlaceholderText('Username') 
        self.setSizePolicy(modules.QSizePolicy.Preferred, modules.QSizePolicy.Preferred)  
        self.setStyleSheet('''
        border-radius: 15px;
        background-color: rgb(210, 210, 210);
        ''')   

        
