from Client import Client


class HTTPClient(Client):
    def __init__(self, source, timeout):
        super().__init__(source, timeout)

    def welcomeAfterConnection(self):
        return self.connect() + " From HTTP Class"
