from Client import Client


class TCPClient(Client):
    def __init__(self, source, timeout, portNumber):
        super().__init__(source, timeout)
        self._portNumber = portNumber
