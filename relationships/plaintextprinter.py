from printer import Printer


class PlainTextPrinter(Printer):
    def __init__(self, message):
        super().__init__(message)

    def welcome(self):
        return "This is a plain text format of the string: {}".format(self._message)
