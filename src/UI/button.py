from enum import Enum

class Type(Enum):
    MENU = 1,
    CHAT = 2,
    PROFILE = 3


class ButtonStyleSheets:
    default = '''
        QPushButton{
            border:none;
        }
        QPushButton:hover{
            border-top: 10px solid white;
            border-left: 5px solid rgb(229, 229, 229);
            border-right: 5px solid rgb(229, 229, 229);
            border-bottom: 10px solid white;
        }    
    '''