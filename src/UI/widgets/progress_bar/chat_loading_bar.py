import modules

class ChatLoadingBar(modules.QProgressBar):
    def __init__(self) -> None:
        super().__init__()

        self.setSizePolicy(modules.QSizePolicy.Ignored, modules.QSizePolicy.Ignored)

        self.setRange(0,0)

        
