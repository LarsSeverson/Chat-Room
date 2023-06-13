import modules

class ConnectionCheckThread(modules.QThread):
    viability_checked = modules.pyqtSignal(bool)

    def __init__(self, ip: str, port: int) -> None:
        super().__init__()

        self.ip = ip
        self.port = port

    def run(self):
        is_viable = self.check_connection(self.ip, self.port)
        self.viability_checked.emit(is_viable)

    def check_connection(self, ip = '127.0.0.1', port = 1234):
        try:
            modules.socket.create_connection((ip, port), timeout=5)
            return True
        except modules.socket.error:
            return False