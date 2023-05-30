import modules

class ChatType(modules.Enum):
    SENDER = 1,
    RECEIVER = 2

class Chat:
    def __init__(self) -> None:
        pass

    def text_message(self, text):
        print(text)