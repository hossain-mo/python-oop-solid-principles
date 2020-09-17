from printer import Printer


class HTMLPrinter(Printer):
    def __init__(self, message):
        super().__init__(message)

    def welcome(self):
        return "<h1>This is a HTML format of the string: {}</h1>".format(self._message)
