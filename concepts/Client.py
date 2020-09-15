class Client:
    def __init__(self, source, timeout):
        self._source = source
        self._timeout = timeout

    def connect(self):
        return "The Client was connected"

    def call(self, url):
        return "Hello {}".format(url)

    def terminate(self):
        return "The Client Was Terminated"
